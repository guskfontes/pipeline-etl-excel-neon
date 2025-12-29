import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# ==========================================================
# 1. CONFIGURAÇÃO (JÁ PREENCHI PARA VOCÊ)
# ==========================================================
# Link recuperado da sua imagem anterior
LINK_DO_SEU_NEON = "postgresql://neondb_owner:npg_1NxFtAUo7crp@ep-soft-voice-ad5of3e0-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require"

def carregar_excel():
    print("📂 Lendo Excel...")
    df_assoc = pd.read_excel('assp_origem.xlsx', sheet_name='Associados')
    df_doac = pd.read_excel('assp_origem.xlsx', sheet_name='Doacoes')
    return df_assoc, df_doac

def processar_e_salvar(df_associados, df_doacoes):
    print("☁️ Conectando no Neon...")
    engine = create_engine(LINK_DO_SEU_NEON)
    
    # ------------------------------------------------------
    # PARTE A: Salvar Associados
    # ------------------------------------------------------
    print("💾 Salvando Associados...")
    try:
        df_associados.to_sql('associados', engine, if_exists='append', index=False)
    except Exception as e:
        print("⚠️ Aviso: Alguns associados já existiam.")

    # ------------------------------------------------------
    # PARTE B: Buscar IDs no Banco
    # ------------------------------------------------------
    print("🔍 Buscando os IDs que o banco criou...")
    df_banco = pd.read_sql("SELECT id_associado, email FROM associados", engine)
    
    # Cruza (Merge) o Excel de Doações com os IDs do Banco
    print("🔄 Cruzando dados...")
    df_final = pd.merge(df_doacoes, df_banco, left_on='email_associado', right_on='email')
    
    # ------------------------------------------------------
    # PARTE C: Preparar Doação
    # ------------------------------------------------------
    df_final['data_doacao'] = datetime.now().date()
    
    # Seleciona só as colunas certas para o banco
    df_para_banco = df_final[['id_associado', 'valor', 'metodo', 'data_doacao']]
    
    # ------------------------------------------------------
    # PARTE D: Salvar Doações
    # ------------------------------------------------------
    print(f"💾 Salvando {len(df_para_banco)} doações corretas...")
    df_para_banco.to_sql('doacoes', engine, if_exists='append', index=False)
    
    print("✅ Sucesso Total! Pipeline finalizado.")

if __name__ == "__main__":
    try:
        assocs, doacoes = carregar_excel()
        processar_e_salvar(assocs, doacoes)
    except Exception as e:
        print(f"❌ Erro: {e}")