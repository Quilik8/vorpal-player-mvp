# REGISTRO TÉCNICO DEL PROYECTO: VORPAL BUILDER

## 1. Objetivo del Proyecto

El objetivo es establecer un entorno de desarrollo automatizado capaz de ejecutar un script de Python (`generar_plan.py`) que utiliza el framework de agentes de IA `crewai` para procesar una serie de documentos de texto.

---

## 2. Historial de Estrategias de Configuración Fallidas

Este registro documenta los enfoques que se han intentado y las razones por las que han fracasado. El objetivo es evitar la repetición de estos errores.

### Intento #1: Entorno Local (Conda + Pip)

*   **Estrategia:** Configuración manual de un entorno Conda en un sistema operativo Windows, seguida de la instalación de paquetes a través de `pip`.
*   **Resultado:** Se encontraron múltiples errores irresolubles:
    1.  `PermissionDenied`: Errores de permisos de escritura de `pip` en Windows.
    2.  `NoMatchingDistribution`: Ciertas versiones de paquetes no tenían distribuciones compatibles con Windows o la versión de Python utilizada.
    3.  `ResolutionImpossible`: Conflictos de dependencias que `pip` no pudo resolver automáticamente.
*   **Análisis del Fallo:** La configuración de entornos de Python en Windows es inherentemente frágil. La combinación de Conda y Pip, junto con las dependencias complejas del ecosistema de IA (especialmente `langchain`), demostró ser inestable y difícil de depurar.

### Intento #2: Automatización con GitHub Actions y Poetry

*   **Estrategia:** Se abandonó el entorno local en favor de un entorno automatizado en la nube utilizando GitHub Actions. Se utilizó el gestor de dependencias `Poetry` con un archivo `pyproject.toml` para definir los requisitos.
*   **Resultado:** Se produjo un ciclo de fallos de `version solving failed` dentro del workflow de GitHub Actions.
*   **Análisis del Fallo:** La estrategia consistió en intentar "adivinar" manualmente un conjunto de versiones compatibles en el archivo `pyproject.toml`. Este enfoque es ineficaz debido a la extrema complejidad y volatilidad del árbol de dependencias de `crewai` y `langchain`. Cada corrección manual a una versión provocaba un nuevo conflicto en una sub-dependencia diferente. La estrategia en sí era un ciclo de ensayo y error, no un proceso de construcción determinista.

---

## 3. Conclusión Estratégica y Próximos Pasos

*   **Análisis Final:** La causa raíz de todos los fallos ha sido intentar construir un entorno de dependencias desde cero, ya sea de forma manual o con scripts, sin partir de una base verificada. La filosofía de "reparación reactiva" ha demostrado ser un fracaso.
*   **Nueva Filosofía de Trabajo:** La nueva estrategia será la **"Replicación de Plantillas Verificadas"**. En lugar de inventar una configuración, se adoptará y adaptará la estructura completa de un proyecto de plantilla (`starter kit`) oficial de `crewai` que esté garantizado para funcionar.
*   **Próxima Acción:** El siguiente paso será reestructurar el repositorio `Vorpal_Builder` para que refleje la estructura de una de estas plantillas, utilizando un enfoque de contenedorización más robusto (como `Dockerfile` junto con `devcontainer.json`).