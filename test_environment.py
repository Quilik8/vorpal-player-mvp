import os
from dotenv import load_dotenv

print("Iniciando prueba de entorno...")

try:
    # 1. Probar importaciones clave
    from crewai import Agent
    from langchain_google_genai import ChatGoogleGenerativeAI
    print("-> [ÉXITO] Las librerías principales (crewai, langchain-google-genai) se importaron correctamente.")

    # 2. Probar la carga de variables de entorno
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")

    if api_key and len(api_key) > 10:
        print("-> [ÉXITO] La variable de entorno GOOGLE_API_KEY se cargó correctamente.")
    else:
        print("-> [FALLO] No se pudo cargar la variable de entorno GOOGLE_API_KEY desde el archivo .env.")
        exit(1)

    # 3. Probar la inicialización del modelo de lenguaje
    llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
    print("-> [ÉXITO] El modelo de lenguaje (LLM) se inicializó correctamente.")
    
    print("\nPrueba de entorno completada con éxito. El sistema está listo.")

except ImportError as e:
    print(f"\n-> [FALLO CATASTRÓFICO] Una librería esencial no está instalada: {e}")
except Exception as e:
    print(f"\n-> [FALLO INESPERADO] Ocurrió un error durante la prueba: {e}")