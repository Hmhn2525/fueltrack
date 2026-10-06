# Verificación y límites

Fecha: 2026-10-05.

## Fuente local

El 5 de octubre de 2026 se ejecutaron nuevamente 65 pruebas locales simuladas: 65 correctas, cero fallos. Cubren autorización, saldos, fallos de almacenamiento, reintentos, consultas y conservación offline. La simulación no mide latencia de Google.

Las fuentes privadas se conservaron. Las ubicaciones y huellas revisadas se registran en la ficha de gestión local; no se copian documentos internos ni rutas operativas al repositorio público. Las pruebas originales no se distribuyen, por lo que este repositorio no permite reproducir su suite.

## Material público reproducible

`python examples/verify.py` comprueba la identificación sintética, el saldo aritmético y el valor esperado de descuento adicional (0 L adicionales) en un escenario sintético. Este script no ejecuta solicitudes repetidas ni valida el mecanismo operativo de idempotencia en red. El recorrido HTML es autónomo, no solicita datos externos y permite avanzar por las etapas explicativas mediante teclado.

## Condiciones no acreditadas

- Integración en una copia de Sheets y una carpeta Drive de pruebas.
- Comparación del código desplegado, permisos y activadores reales.
- Pruebas de dispositivos, red interrumpida y actualización de una PWA instalada.
- Aceptación humana de fotografías y firmas; decisión de licencia en su fase técnica propia.

Un repositorio publicado y un ejemplo correcto no certifican operación productiva ni aceptación de usuarios.
