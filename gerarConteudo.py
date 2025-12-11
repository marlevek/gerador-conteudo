import streamlit as st
import streamlit.components.v1 as components 
from dotenv import load_dotenv 
from langchain_openai import ChatOpenAI 
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser 


# Carrega variáveis de ambiente (para uso local)
load_dotenv()


# ==============================
# Função botão "Copiar"
# ==============================
def botao_copiar(texto: str, label: str = "📋 Copiar texto gerado"):
    components.html(
        f"""
        <button onclick="
            navigator.clipboard.writeText(`{texto}`);
            this.innerText = '✅ Copiado!';
            setTimeout(() => this.innerText = '{label}', 2000);
        " style="
            padding: 0.5rem 1rem;
            border-radius: 6px;
            border: 1px solid #ccc;
            cursor: pointer;
            background-color: #f0f2f6;
        ">
            {label}
        </button>
        """,
        height=50,
    )

# ==============================
# Função para obter LLM da OpenAI
# ==============================
def get_llm(model_id: str, temperature: float):
    """
    model_id: ex. 'gpt-4.1-mini', 'gpt-4.1', etc.
    """
    return ChatOpenAI(
        model=model_id,
        temperature=temperature,
        max_retries=2,
    )


# ==============================
# Função de geração de conteúdo
# ==============================
def llm_generate(
    llm,
    tema: str,
    plataforma: str,
    tom: str,
    tamanho: str,
    publico: str,
    incluir_cta: bool,
    incluir_hashtags: bool,
    palavras_chave: str,
    nicho: str,
):
    system_prompt = """
Você é um especialista em marketing digital com foco em SEO, copywriting e escrita persuasiva.
Você escreve sempre em português do Brasil, em linguagem clara, moderna e escaneável.
Adapte o texto ao nicho informado, ao tipo de público e à plataforma escolhida.
Traga ideias específicas, práticas e aplicáveis para o contexto do cliente.
Nicho do cliente: {nicho}
"""

    user_prompt = f"""
Escreva um conteúdo com SEO otimizado sobre o tema: '{tema}'.

- Plataforma onde será publicado: {plataforma}
- Tom do texto: {tom}
- Público-alvo: {publico}
- Comprimento desejado: {tamanho}
- {"Inclua uma chamada para ação clara e forte ao final." if incluir_cta else "Não inclua chamada para ação."}
- {"Inclua ao final do texto uma lista de hashtags relevantes para esta publicação." if incluir_hashtags else "Não inclua hashtags."}
{f"- Palavras-chave obrigatórias para SEO: {palavras_chave}" if palavras_chave else ""}

Regras importantes da resposta:
1. Entregue apenas o texto final (sem explicar o passo a passo).
2. Não use aspas envolvendo o texto inteiro.
3. Estruture o conteúdo em parágrafos curtos e, se fizer sentido, use listas ou bullets.
"""

    template = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{user_prompt}"),
        ]
    )

    chain = template | llm | StrOutputParser()

    res = chain.invoke(
        {
            "nicho": nicho or "negócios locais",
            "user_prompt": user_prompt,
        }
    )
    return res


# ==============================
# Configuração da página
# ==============================
st.set_page_config(
    page_title="Gerador de Conteúdo com IA",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 Gerador de conteúdo com IA para negócios")
st.caption("Focado em SEO, copy persuasiva e posts prontos para redes sociais.")


# ==============================
# Sidebar – Configuração da IA (OpenAI)
# ==============================
with st.sidebar:
    st.header("⚙️ Configurações da IA")

    # Aqui você pode ajustar para os modelos que você tem acesso na OpenAI
    modelo_opcao = st.selectbox(
        "Modelo OpenAI:",
        [
            "gpt-4.1-mini",
            "gpt-4.1",
        ],
    )

    temperatura = st.slider(
        "Criatividade (temperature):",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.05,
        help="Valores mais baixos = mais objetivo; valores mais altos = mais criativo.",
    )

    st.markdown("---")
    st.markdown("**Dica:** use nichos específicos (ex.: “clínica de psicologia”, “empresa de ar-condicionado”).")

# Inicializa histórico
if "historico" not in st.session_state:
    st.session_state.historico = []


# ==============================
# Layout: formulário + histórico
# ==============================
col_form, col_hist = st.columns([2, 1])

with col_form:
    st.subheader("🧾 Briefing do conteúdo")

    nicho = st.text_input(
        "Nicho / Tipo de negócio:",
        placeholder="Ex: clínica de psicologia, consultório odontológico, empresa de ar-condicionado...",
    )

    topic = st.text_input(
        "Tema do conteúdo:",
        placeholder="Ex: saúde mental, manutenção preventiva de ar-condicionado, alimentação saudável...",
    )

    platform = st.selectbox(
        "Plataforma:",
        ["Instagram", "Facebook", "LinkedIn", "Blog", "E-mail", "YouTube (descrição de vídeo)"],
    )

    tone = st.selectbox("Tom:", ["Normal", "Informativo", "Inspirador", "Urgente", "Informal", "Educativo"])

    length = st.selectbox("Tamanho:", ["Curto", "Médio", "Longo"])

    audience = st.selectbox(
        "Público-alvo:",
        ["Geral", "Jovens adultos", "Famílias", "Idosos", "Adolescentes", "Empresários", "Profissionais da saúde"],
    )

    cta = st.checkbox("Incluir CTA (chamada para ação)")
    hashtags = st.checkbox("Incluir hashtags")

    keywords = st.text_area(
        "Palavras-chave (SEO):",
        placeholder="Ex: bem-estar, medicina preventiva, manutenção preventiva, PMOC...",
    )

    gerar = st.button("🚀 Gerar conteúdo", type="primary")

    if gerar:
        if not topic:
            st.warning("Informe pelo menos o tema do conteúdo.")
        else:
            try:
                llm = get_llm(modelo_opcao, temperatura)

                res = llm_generate(
                    llm=llm,
                    tema=topic,
                    plataforma=platform,
                    tom=tone,
                    tamanho=length,
                    publico=audience,
                    incluir_cta=cta,
                    incluir_hashtags=hashtags,
                    palavras_chave=keywords,
                    nicho=nicho,
                )

                st.success("✅ Conteúdo gerado com sucesso!")

                st.text_area(
                    "📝 Conteúdo gerado:",
                    value=res,
                    height=350,
                    key="conteudo_gerado",
                )

                botao_copiar(res)

                # Salvar no histórico
                st.session_state.historico.append(
                    {
                        "tema": topic,
                        "plataforma": platform,
                        "tom": tone,
                        "público": audience,
                        "tamanho": length,
                        "texto": res,
                        "modelo": modelo_opcao,
                        "nicho": nicho,
                    }
                )

            except Exception as e:
                st.error(f"Erro ao chamar a IA: {e}")


# ==============================
# Histórico
# ==============================
with col_hist:
    st.subheader("📚 Histórico de conteúdos")

    if st.session_state.historico:
        for i, item in enumerate(reversed(st.session_state.historico), 1):
            with st.expander(f"{i}. {item['tema']} ({item['plataforma']}) – {item['modelo']}"):
                if item.get("nicho"):
                    st.markdown(f"**Nicho:** {item['nicho']}")
                st.markdown(f"**Tom:** {item['tom']}")
                st.markdown(f"**Público-alvo:** {item['público']}")
                st.markdown(f"**Tamanho:** {item['tamanho']}")
                st.markdown("**Texto gerado:**")
                st.markdown(item["texto"])
    else:
        st.info("Nenhum conteúdo gerado ainda.")  