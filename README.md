# Estimación MCO
Script que permite estimar los parámetros de interés a través de MCO (mínimos cuadrados ordinarios). 

## Método de uso
Ingresar las desviaciones separas por comas y los niveles de madurez tambien separados por comas (no se deben incluir espacios en ninguno). El script genera los parámetros de interés más un gráfico que proyecta las predicciones de acuerdo a la escala para medir madurez (en este caso es la escala propuesta por Succar, con rating de 1 a 4).

Si se quiere un cuadro resumen tipo Stata, escribir reg.summary()
