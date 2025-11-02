# --- INICIO DEL PARCHE SQLITE3 ---
try:
    __import__('pysqlite3')
    import sys
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
except ImportError:
    pass # La ejecución posterior fallará si es necesario, pero no detenemos el script aquí.
# --- FIN DEL PARCHE SQLITE3 ---

import os
import re
from dotenv import load_dotenv

# Importaciones de CrewAI y LangChain
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI

# --- FASE DE CONFIGURACIÓN ---
print("Iniciando la configuración del script...")

# 1. Cargar las variables de entorno
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("ERROR: La variable 'GOOGLE_API_KEY' no se encontró en el archivo .env.")
    exit()

# 2. Configurar el modelo de lenguaje (LLM)
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini 2.5 pro",
        verbose=True,
        temperature=0.5,
        google_api_key=api_key
    )
    print("-> [ÉXITO] Modelo de lenguaje (LLM) configurado.")
except Exception as e:
    print(f"ERROR: No se pudo inicializar el LLM. Detalles: {e}")
    exit()

# --- FUNCIONES DE AYUDA ---

def leer_archivo(nombre_archivo):
    """Lee el contenido de un archivo de forma segura."""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"ADVERTENCIA: No se encontró el archivo '{nombre_archivo}'.")
        return ""

def guardar_archivo(ruta_carpeta, nombre_archivo, contenido):
    """Guarda contenido en un archivo, creando la carpeta si no existe."""
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
    ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)
    with open(ruta_completa, 'w', encoding='utf-8') as f:
        f.write(contenido)
    print(f"-> Archivo guardado: {ruta_completa}")

def normalizar_nombre(titulo):
    """Convierte un título de capítulo en un nombre de archivo y carpeta válidos."""
    match_epoca = re.search(r'Época\s+([IVXLCDM]+)', titulo, re.IGNORECASE)
    epoca_id = match_epoca.group(1) if match_epoca else 'Desconocida'
    
    match_cap = re.search(r'(?:Capítulo\s+|(\d+)\.-Análisis)\s*(\d*)', titulo)
    cap_num_group1 = match_cap.group(1) if match_cap and match_cap.group(1) else None
    cap_num_group2 = match_cap.group(2) if match_cap and match_cap.group(2) else None
    cap_num = cap_num_group2 if cap_num_group2 else (cap_num_group1 if cap_num_group1 else 'X')

    nombre_limpio = re.sub(r'[^a-zA-Z0-9\s-]', '', titulo)
    nombre_limpio = re.sub(r'\s+', '_', nombre_limpio)
    partes_nombre = nombre_limpio.split('_')
    nombre_corto = '_'.join(partes_nombre[3:7]) if len(partes_nombre) > 6 else '_'.join(partes_nombre[3:])

    carpeta = f"Epoca_{epoca_id}"
    archivo = f"Epoca_{epoca_id}-Capitulo_{cap_num}_{nombre_corto}.md"
    
    return carpeta, archivo

# --- CARGA DE CONTEXTO ---
print("\nCargando archivos de contexto...")
documentos_contexto = {
    'directivas_maestras': leer_archivo('DIRECTIVAS_MAESTRAS.md'),
    'plan_de_negocio': leer_archivo('Vorpal_Business_Plan.md'),
    'principios_de_diseno': leer_archivo('Principios de diseño.md'),
    'blueprint_wolrdforge': leer_archivo('Blueprint base wolrdforge.md'),
    'guia_vorpal_para_estructura': leer_archivo('guia Vorpal para estructura.md')
}
if not documentos_contexto['directivas_maestras'] or not documentos_contexto['guia_vorpal_para_estructura']:
    print("ERROR: Los archivos 'DIRECTIVAS_MAESTRAS.md' y 'guia Vorpal para estructura.md' son esenciales.")
    exit()
print("-> [ÉXITO] Todos los archivos de contexto cargados.")

# --- DEFINICIÓN DE AGENTES (La Crew) ---
print("\nDefiniendo el equipo de agentes de IA...")
agentes = {
    'contextualizador': Agent(
        role='Contextualizador Estratégico',
        goal='Leer un capítulo y los documentos de referencia, y compilar un paquete de contexto conciso.',
        backstory='Eres el bibliotecario del proyecto Vorpal, con dominio absoluto de todos los documentos.',
        llm=llm, verbose=True
    ),
    'sintetizador_redactor': Agent(
        role='Sintetizador-Redactor',
        goal='Recibir un contexto y ensamblar un documento Markdown detallado y bien estructurado, siguiendo las directivas.',
        backstory='Eres un editor técnico meticuloso. No creas contenido, lo perfeccionas y estructuras. Eres el control de calidad final.',
        llm=llm, verbose=True, allow_delegation=False
    )
}
print("-> [ÉXITO] Equipo de agentes definido.")

# --- PROCESO PRINCIPAL ---
print("\nIniciando el proceso de automatización...")

capitulos = re.split(r'\n(?=\d+\.-Análisis Detallado)', documentos_contexto['guia_vorpal_para_estructura'])
if len(capitulos) <= 1:
    print("ERROR: No se pudieron encontrar secciones de capítulo en 'guia Vorpal para estructura.md'.")
    exit()

for i, texto_capitulo in enumerate(capitulos):
    if not texto_capitulo.strip() or "Análisis Detallado" not in texto_capitulo:
        continue

    titulo_capitulo = texto_capitulo.strip().split('\n')[0]
    print(f"\n=============================================")
    print(f"Procesando: {titulo_capitulo}")
    print(f"=============================================")

    crew_capitulo = Crew(
        agents=list(agentes.values()),
        tasks=[],
        process=Process.sequential,
        verbose=2
    )
    
    task_contexto = Task(
        description=f"Analiza el siguiente texto del capítulo '{titulo_capitulo}' y el contexto global de los documentos del proyecto para crear un resumen contextual completo. Texto del capítulo: '{texto_capitulo}'",
        agent=agentes['contextualizador'],
        expected_output="Un documento de texto con el resumen del capítulo, sus objetivos principales y las directivas más relevantes para su desarrollo."
    )
    
    task_completa = Task(
        description=f"Toma el contexto proporcionado sobre el capítulo '{titulo_capitulo}' y, utilizando el conocimiento de TODOS los documentos del proyecto, detallalo completamente. Debes seguir la estructura especificada en las DIRECTIVAS_MAESTRAS.md (Acciones Concretas, Entregables, Riesgos, etc.).",
        agent=agentes['sintetizador_redactor'],
        context=[task_contexto],
        expected_output="El contenido completo y final del capítulo en formato Markdown."
    )

    crew_capitulo.tasks.extend([task_contexto, task_completa])

    resultado_generado = crew_capitulo.kickoff(inputs=documentos_contexto)
    
    print(f"--- Generación completa para '{titulo_capitulo}' ---")
    
    # Guardar el resultado
    carpeta_salida, archivo_salida = normalizar_nombre(titulo_capitulo)
    guardar_archivo(carpeta_salida, archivo_salida, resultado_generado)

print("\n=============================================")
print("PROCESO DE GENERACIÓN COMPLETADO.")
print("Revisa las nuevas carpetas 'Epoca_X' para ver los archivos .md detallados.")
print("=============================================")