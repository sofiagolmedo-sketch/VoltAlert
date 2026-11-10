import streamlit as st
import random

# Configuración visual de la aplicación
st.title("⚡ VoltAlert - Sistema Predictivo Inteligente")
st.write("Panel de control y mitigación de sobrecargas barriales (Enfoque CTS).")

st.markdown("---")

# 1. Configuración de la lista de difusión comunitaria (un correo por línea)
st.subheader("Configuración de Alertas y Difusión Masiva")
correos_input = st.text_area(
    "Correos de los vecinos y municipio (escribe un correo por línea):", 
    "vecino.zona1@gmail.com\ncomercio.centro@gmail.com\nguardia.municipal@gmail.com\nhogar.familia.perez@gmail.com"
)

lista_destinatarios = [c.strip() for c in correos_input.split("\n") if c.strip()]

st.markdown("---")

# 2. Controles interactivos para la demostración en vivo
st.subheader("Simulación de Condiciones Climáticas (Ola de Calor)")
col1, col2 = st.columns(2)

with col1:
    temp_ingresada = st.slider("Temperatura ambiente (°C):", 15.0, 45.0, 28.5)
with col2:
    hora_ingresada = st.slider("Hora del día (hs):", 0, 23, 15)

# 3. Lógica calibrada: a partir de los 28°C en hora pico se cruzan los 500 kW
consumo_base = 200
pico_horario = 160 if 13 <= hora_ingresada <= 19 else 0

# Si llega a 28°C o más, el encendido masivo de aires suma un factor de salto crítico
if temp_ingresada >= 28.0:
    factor_calor = (temp_ingresada - 27) * 45.0
else:
    factor_calor = 0.0

prediccion_pico = consumo_base + (temp_ingresada * 4.0) + factor_calor + pico_horario
UMBRAL_CRITICO = 500  # kW límite del transformador barrial

# 4. Mostrar resultados visuales y despacho masivo
st.markdown("---")
st.metric(label="Predicción de Demanda del Transformador (IA)", value=f"{prediccion_pico:.1f} kW")

if prediccion_pico > UMBRAL_CRITICO:
    st.error("🚨 ¡ALERTA ROJA DE SOBRECARGA DETECTADA!")
    st.write(f"**Riesgo crítico:** El consumo estimado supera los {UMBRAL_CRITICO} kW habilitados para esta fase.")
    
    st.info(f"📧 **Difusión masiva ejecutada con éxito.** Se dispararon alertas automáticas a **{len(lista_destinatarios)} destinatarios** de la red:")
    for correo in lista_destinatarios:
        st.write(f"✔️ *Enviado a:* `{correo}`")
        
    st.warning("💬 *Mensaje emitido:* 'Alerta VoltAlert: Se prevé un pico crítico de consumo en tu zona. Por favor posponga el uso de electrodomésticos de alto consumo para evitar cortes en el barrio.'")
else:
    st.success("✅ Estado de la Red: Normal. El modelo no detecta riesgo inminente de sobrecarga.")