import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mon Programme RTG 2026", page_icon="⏱️", layout="centered")

st.title("🫀 My Personal RTG 2026 Schedule")
st.markdown("Alege sesiunile la care vrei să participi pentru a ști exact în ce sală să mergi.")

# Baza de date cu programul extras din PDF (Aperçu)
schedule_data = {
    "Mardi 31 Mars 2026": {
        "08h30 - 09h30": [
            "Salle Louis ARMAND | GACI Basic: Maîtriser les voies d'abord",
            "Salle Friedrich LIST | GACI Advanced: Imagerie endocoronaire",
            "Salle George STEPHENSON | GACI Expert: TAVI dans les situations particulières"
        ],
        "09h40 - 10h40": [
            "Salle Louis ARMAND | SESSION COMMUNE: Controverses dans les SCA"
        ],
        "11h10 - 12h10": [
            "Salle Louis ARMAND | GACI Basic: Physiologie coronaire",
            "Salle Friedrich LIST | Session TUC: AVC / GACI Advanced: Bifurcations",
            "Salle George STEPHENSON | GACI Expert: Occlusions coronaires / Session TUC: Thrombose"
        ],
        "13h30 - 14h45": [
            "Salle Louis ARMAND | Atelier débat Medtronic: Traiter une bifurcation"
        ],
        "15h00 - 16h00": [
            "Salle Louis ARMAND | SESSION COMMUNE: Valvulopathies",
            "Salle George STEPHENSON | ATELIER PARAMED: Défi ECG"
        ],
        "16h30 - 17h30": [
            "Salle Louis ARMAND | SESSION COMMUNE: Antiagrégants plaquettaires parentéraux"
        ],
        "17h45 - 18h45": [
            "Salle Louis ARMAND | GACI Advanced: Mon angioplastie se complique",
            "Salle Friedrich LIST | SESSION TUC: Ablation de la FA",
            "Salle George STEPHENSON | GACI Expert: Mon TAVI se complique"
        ],
        "19h00 - 21h30": [
            "Toutes les Salles | Soirée Simulation GACI (Ateliers pratiques)"
        ]
    },
    "Mercredi 1er Avril 2026": {
        "08h30 - 09h30": [
            "Salle Louis ARMAND | GACI Basic: Coronarographies complexes / Session Commune",
            "Salle Friedrich LIST | SESSION TUC: HTA",
            "Salle George STEPHENSON | GACI Expert: Réparation mitrale"
        ],
        "09h40 - 10h40": [
            "Salle George STEPHENSON | ATELIER PARAMED: Le quiz des médicaments"
        ],
        "11h10 - 12h25": [
            "Salle Louis ARMAND | GACI Basic: Bifurcations",
            "Salle Friedrich LIST | GACI Advanced: Mon premier TAVI"
        ],
        "12h35 - 13h50": [
            "Salle Louis ARMAND | SESSION COMMUNE: Choc cardiogénique du STEMI"
        ],
        "14h00 - 15h00": [
            "Salle Louis ARMAND | GACI Advanced: Lésions calcifiées",
            "Salle Friedrich LIST | SESSION TUC: Insuffisance cardiaque",
            "Salle George STEPHENSON | GACI Expert: TAVI avec abords complexes"
        ],
        "15h30 - 16h30": [
            "Salle Louis ARMAND | SESSION COMMUNE: Arrêt cardiaque - Place de l'IA"
        ],
        "16h40 - 17h40": [
            "Salle Louis ARMAND | GACI Basic: L'angoisse de mes premières astreintes",
            "Salle Friedrich LIST | GACI Advanced: Traitements percutanés de l'embolie pulmonaire",
            "Salle George STEPHENSON | SESSION TUC: Atelier ECG"
        ],
        "17h45 - 18h45": [
            "Salle Louis ARMAND | GACI Basic: Les lésions pluritronculaires",
            "Salle Friedrich LIST | GACI Advanced: Angioplastie au ballon actif",
            "Salle George STEPHENSON | GACI Expert: Réparation tricuspide"
        ]
    }
}

# Creăm tab-uri pentru cele două zile
tab_mardi, tab_mercredi = st.tabs(["Mardi 31 Mars", "Mercredi 1er Avril"])

# Dicționar pentru a salva alegerile tale
my_schedule = {}

def build_day_schedule(day_name, data):
    st.header(f"📅 {day_name}")
    for time_slot, options in data.items():
        # Adăugăm opțiunea de a nu merge la nimic în acel interval
        choices = ["☕ Pauză / Nu particip"] + options
        
        # Selectbox pentru fiecare oră
        selected = st.selectbox(
            f"🕒 {time_slot}", 
            options=choices,
            key=f"{day_name}_{time_slot}"
        )
        if selected != "☕ Pauză / Nu particip":
            my_schedule[f"{day_name} | {time_slot}"] = selected

with tab_mardi:
    build_day_schedule("Mardi 31 Mars 2026", schedule_data["Mardi 31 Mars 2026"])

with tab_mercredi:
    build_day_schedule("Mercredi 1er Avril 2026", schedule_data["Mercredi 1er Avril 2026"])

st.markdown("---")
st.header("📋 Itinerarul Meu Final")

if my_schedule:
    st.success("Iată programul tău! Fă un screenshot sau lasă pagina deschisă pe telefon.")
    for time_key, session in my_schedule.items():
        day, time = time_key.split(" | ")
        # Extragem sala pentru a o evidenția
        sala, titlu = session.split(" | ")
        
        st.markdown(f"**{day} - {time}**")
        st.markdown(f"📍 **{sala}** ➡️ {titlu}")
        st.markdown("") # Spațiu
else:
    st.info("Încă nu ai selectat nicio sesiune. Alege sesiunile de mai sus pentru a-ți construi programul.")
    
