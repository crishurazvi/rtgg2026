import streamlit as st

# 1. Configurarea paginii (trebuie să fie prima comandă Streamlit)
st.set_page_config(
    page_title="Rencontres TUC-GACI 2026",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS Personalizat pentru un design ultra-modern
st.markdown("""
    <style>
    .main-title {
        font-size: 3rem;
        color: #E63946;
        text-align: center;
        font-weight: bold;
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 1.5rem;
        color: #1D3557;
        text-align: center;
        margin-bottom: 30px;
    }
    .info-box {
        background-color: #F1FAEE;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #457B9D;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Antetul Paginii
st.markdown('<p class="main-title">Rencontres TUC-GACI 2026</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Le rendez-vous de la cardiologie interventionnelle, des urgences coronaires et de la thrombose</p>', unsafe_allow_html=True)

# 4. Crearea Tab-urilor pentru navigare
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Accueil", "📅 Programme", "🩺 Soirée Simulation", "📍 Infos Pratiques"])

# --- TAB 1: ACCUEIL ---
with tab1:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### Bienvenue aux Rencontres TUC-GACI 2026 !")
        st.write("""
        C'est avec grand plaisir que le comité d'organisation vous accueille à cette nouvelle édition. 
        Un rendez-vous incontournable pour tous les acteurs de la cardiologie interventionnelle, 
        des urgences coronaires et des facteurs de risques cardio-métaboliques.
        """)
        st.info("💡 **Partenaires institutionnels:** Société Française de Cardiologie, SAMU, Société Française de Médecine d'Urgence.")
        
    with col2:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("🗓️ **Dates :** 31 Mars & 1er Avril 2026")
        st.markdown("📍 **Lieu :** UIC-P Espaces Congrès, Paris")
        st.markdown("✅ **Éthique :** Conforme Ethical MEDTECH (EMT-26-09248)")
        st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 2: PROGRAMME ---
with tab2:
    st.markdown("### Aperçu du Programme Scientifique")
    st.write("Découvrez les sessions plénières, les parcours GACI (Basic, Advanced, Expert) et les sessions TUC.")
    
    jour1, jour2 = st.columns(2)
    
    with jour1:
        st.subheader("Mardi 31 Mars 2026")
        with st.expander("08h30 - 10h40 : Sessions Matinales"):
            st.markdown("""
            * **GACI Basic:** Maîtriser les voies d'abord
            * **GACI Advanced:** Imagerie endocoronaire
            * **GACI Expert:** TAVI dans les situations particulières
            * **Session Commune:** Controverses dans les SCA
            """)
        with st.expander("11h10 - 13h20 : Milieu de Journée"):
            st.markdown("""
            * **GACI Basic:** Physiologie coronaire
            * **GACI Advanced:** Bifurcations (cas complexes)
            * **Session TUC:** AVC, Thrombose dans tous ses états
            """)
        with st.expander("15h00 - 18h45 : Après-midi"):
            st.markdown("""
            * **Session Commune:** Valvulopathies
            * **Session Commune:** Antiagrégants plaquettaires parentéraux
            * **Session TUC:** Ablation de la FA
            """)

    with jour2:
        st.subheader("Mercredi 1er Avril 2026")
        with st.expander("08h30 - 10h40 : Sessions Matinales"):
            st.markdown("""
            * **GACI Basic:** Coronarographies (situations complexes)
            * **GACI Expert:** Ma première réparation mitrale bord à bord
            * **Session TUC:** HTA - Quoi de neuf ?
            """)
        with st.expander("11h10 - 13h50 : Milieu de Journée"):
            st.markdown("""
            * **GACI Basic:** Bifurcations (fondamentaux)
            * **GACI Advanced:** Mon premier TAVI
            * **Session Commune:** Choc cardiogénique du STEMI
            """)
        with st.expander("14h00 - 18h45 : Après-midi"):
            st.markdown("""
            * **GACI Advanced:** Lésions calcifiées
            * **Session TUC:** Insuffisance cardiaque
            * **Session Commune:** Arrêt cardiaque & IA
            """)

# --- TAB 3: SOIRÉE SIMULATION ---
with tab3:
    st.markdown("### Soirée Simulation GACI")
    st.warning("⏱️ **Date et Heure :** Mardi 31 Mars, 19h00 - 21h30 | 🔄 **Rotation :** Toutes les 30 min (Max 4 ateliers / participant)")
    
    col_sim1, col_sim2 = st.columns(2)
    with col_sim1:
        st.success("**ABBOTT (Salle Louis ARMAND)**")
        st.write("- Fermeture de FOP avec Amplatzer Talisman\n- Navitor sur simulateur à cœur battant\n- Athérectomie Orbitale\n- Bifurcation: provisionnel dans le tronc commun")
        
        st.info("**J&J (Salle Friedrich LIST)**")
        st.write("- Atelier Impella")
        
        st.error("**MEDTRONIC (Salle George STEPHENSON)**")
        st.write("- Lésions de bifurcation - Simulation sur banc")
        
    with col_sim2:
        st.success("**BOSTON SCIENTIFIC (Mezzanine)**")
        st.write("- Lésions calcifiées : l'indispensable Rota\n- Imagerie endocoronaire : adoptez l'IVUS en 3 étapes !")
        
        st.info("**GE HEALTHCARE**")
        st.write("- Formation au post-traitement du scanner cardiaque")
        
        st.error("**THERENVA**")
        st.write("- Sizing TAVI")

# --- TAB 4: INFOS PRATIQUES ---
with tab4:
    col_info1, col_info2 = st.columns(2)
    
    with col_info1:
        st.markdown("### 📍 Comment venir ?")
        st.write("**Adresse :** UIC-P Espaces Congrès, 16 rue Jean Rey, 75015 Paris")
        st.markdown("""
        * **Métro :** Ligne 6, Bir Hakeim
        * **RER :** Ligne C, Champ de Mars
        * **Bus :** 42, 69, 82, 87
        * Accès pour les personnes à mobilité réduite disponible.
        """)
        
    with col_info2:
        st.markdown("### 💶 Frais d'inscription")
        st.write("- **Jusqu'au 28 février 2026 :** 540 €")
        st.write("- **À partir du 1er mars 2026 :** 650 €")
        st.caption("Gratuit pour les ARC, les infirmier(e)s, les étudiants et les internes (sous réserve de présentation d'un justificatif sur place).")
        
        st.markdown("### ✈️ Réduction Air France / KLM")
        st.write("**Code Évènement :** GME60547AF")
        st.write("**Dates de validité :** 24/03/2026 jusqu'au 08/04/2026")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Organisation: LEAD-UP NETWORK | contact@rencontrestucgaci.fr</p>", unsafe_allow_html=True)
