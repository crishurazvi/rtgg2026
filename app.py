import streamlit as st
from collections import OrderedDict

st.set_page_config(
    page_title="Mon Itinéraire Congrès",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# =========================
# Données structurées du programme
# =========================
CONGRESS_DATA = OrderedDict(
    {
        "Mardi 31 mars 2026": OrderedDict(
            {
                "08h30 - 09h30": [
                    {
                        "room": "Louis ARMAND (Plénière)",
                        "session": "GACI Parcours Basic : Maîtriser les voies d’abord",
                    },
                    {
                        "room": "Friedrich LIST",
                        "session": "GACI Parcours Advanced : Imagerie endocoronaire",
                    },
                    {
                        "room": "George STEPHENSON",
                        "session": "GACI Parcours Expert : TAVI dans les situations particulières",
                    },
                ],
                "09h40 - 10h40": [
                    {
                        "room": "Louis ARMAND (Plénière)",
                        "session": "Session commune TUC-GACI : Controverses dans les SCA",
                    },
                ],
                "10h40 - 11h10": [
                    {"room": "Pause", "session": "Pause"},
                ],
                "11h10 - 12h10": [
                    {
                        "room": "Louis ARMAND (Plénière)",
                        "session": "GACI Parcours Expert : Occlusions coronaires chroniques",
                    },
                    {
                        "room": "Friedrich LIST",
                        "session": "Session TUC : AVC, mieux gérer le parcours du patient",
                    },
                    {
                        "room": "George STEPHENSON",
                        "session": "Atelier PARAMED 1 : IC, éducation thérapeutique, télésurveillance et IA",
                    },
                ],
                "12h20 - 13h20": [
                    {
                        "room": "Louis ARMAND (Plénière)",
                        "session": "GACI Parcours Basic : Physiologie coronaire",
                    },
                    {
                        "room": "Friedrich LIST",
                        "session": "GACI Parcours Advanced : Bifurcations, les cas complexes",
                    },
                    {
                        "room": "George STEPHENSON",
                        "session": "Session TUC : Thrombose dans tous ses états, de la prise en charge de l’urgence au suivi à long terme",
                    },
                ],
                "13h20 - 13h30": [
                    {
                        "room": "Transition",
                        "session": "Transition vers salles d’atelier débat / Lunch Bags",
                    },
                ],
                "13h30 - 14h45": [
                    {
                        "room": "Louis ARMAND (Plénière)",
                        "session": "Atelier débat Medtronic : Comment traiter une bifurcation en 2026 ?",
                    },
                    {
                        "room": "George STEPHENSON",
                        "session": "Atelier PARAMED 2 : Défi ECG pour les paramédicaux",
                    },
                ],
                "15h00 - 16h00": [
                    {
                        "room": "Louis ARMAND (Plénière)",
                        "session": "Session commune TUC-GACI : Valvulopathies",
                    },
                ],
                "16h00 - 16h30": [
                    {"room": "Pause", "session": "Pause"},
                ],
                "16h30 - 17h30": [
                    {
                        "room": "Louis ARMAND (Plénière)",
                        "session": "Session commune TUC-GACI : Antiagrégants plaquettaires parentéraux, indications, pratiques et gestion du risque",
                    },
                ],
                "17h45 - 18h45": [
                    {
                        "room": "Louis ARMAND (Plénière)",
                        "session": "GACI Parcours Advanced : Mon angioplastie se complique",
                    },
                    {
                        "room": "Friedrich LIST",
                        "session": "Session TUC : Ablation de la FA, le traitement de référence ?",
                    },
                    {
                        "room": "George STEPHENSON",
                        "session": "GACI Parcours Expert : Mon TAVI se complique",
                    },
                ],
                "19h00 - 21h30": [
                    {
                        "room": "Louis ARMAND (Plénière)",
                        "session": "Soirée Simulation : ABBOTT – Fermeture de FOP avec Amplatzer Talisman / Navitor sur simulateur à cœur battant / Athérectomie orbitale / Bifurcation provisionnel dans le tronc commun",
                    },
                    {
                        "room": "Friedrich LIST",
                        "session": "Soirée Simulation : J&J – Impella",
                    },
                    {
                        "room": "Friedrich LIST",
                        "session": "Soirée Simulation : MEDTRONIC – Lésions de bifurcation, simulation sur banc",
                    },
                    {
                        "room": "George STEPHENSON",
                        "session": "Soirée Simulation : BOSTON SCIENTIFIC – Lésions calcifiées, l’indispensable Rota / Imagerie endocoronaire, adoptez l’IVUS en 3 étapes",
                    },
                    {
                        "room": "Mezzanine",
                        "session": "Soirée Simulation : GE HEALTHCARE – Formation au post-traitement du scanner cardiaque",
                    },
                    {
                        "room": "Salle à préciser",
                        "session": "Soirée Simulation : THERENVA – Sizing TAVI",
                    },
                ],
            }
        ),
        "Mercredi 1er avril 2026": OrderedDict(
            {
                "08h30 - 09h30": [
                    {
                        "room": "Louis ARMAND (Plénière)",
                        "session": "GACI Parcours Basic : Coronarographies, les situations complexes",
                    },
                    {
                        "room": "Friedrich LIST",
                        "session": "Session TUC : HTA, quoi de neuf ?",
                    },
                    {
                        "room": "George STEPHENSON",
                        "session": "GACI Parcours Expert : Ma première réparation mitrale bord à bord",
                    },
                ],
                "09h40 - 10h40": [
                    {
                        "room": "Louis ARMAND (Plénière)",
                        "session": "Session commune TUC-GACI : Cas cliniques, les complications qui enseignent",
                    },
                    {
                        "room": "George STEPHENSON (Bobigny)",
                        "session": "Atelier PARAMED 3 : Le quiz des médicaments de l’urgence cardiologique !",
                    },
                ],
                "10h40 - 11h10": [
                    {"room": "Pause", "session": "Pause"},
                ],
                "11h10 - 12h25": [
                    {
                        "room": "Louis ARMAND (Plénière)",
                        "session": "GACI Parcours Basic : Bifurcations, les fondamentaux",
                    },
                    {
                        "room": "Friedrich LIST",
                        "session": "GACI Parcours Advanced : Mon premier TAVI",
                    },
                    {
                        "room": "George STEPHENSON",
                        "session": "Session TUC : Myocardites / péricardites",
                    },
                ],
                "12h25 - 12h35": [
                    {
                        "room": "Transition",
                        "session": "Transition vers salles d’atelier débat / Lunch Bags",
                    },
                ],
                "12h35 - 13h50": [
                    {
                        "room": "Louis ARMAND (Plénière)",
                        "session": "Session commune TUC-GACI avec soutien institutionnel J&J : Choc cardiogénique du STEMI",
                    },
                    {
                        "room": "George STEPHENSON",
                        "session": "Atelier PARAMED 4 : Angioplastie des lésions calcifiées, comment faire en pratique ?",
                    },
                ],
                "14h00 - 15h00": [
                    {
                        "room": "Louis ARMAND (Plénière)",
                        "session": "GACI Parcours Advanced : Lésions calcifiées",
                    },
                    {
                        "room": "Friedrich LIST",
                        "session": "Session TUC : Insuffisance cardiaque, gestion de la décompensation",
                    },
                    {
                        "room": "George STEPHENSON",
                        "session": "GACI Parcours Expert : TAVI avec abords complexes",
                    },
                ],
                "15h00 - 15h30": [
                    {"room": "Pause", "session": "Pause"},
                ],
                "15h30 - 16h30": [
                    {
                        "room": "Louis ARMAND (Plénière)",
                        "session": "Session commune : Arrêt cardiaque, place de l’IA",
                    },
                ],
                "16h40 - 17h40": [
                    {
                        "room": "Louis ARMAND (Plénière)",
                        "session": "GACI Parcours Basic : L’angoisse de mes premières astreintes",
                    },
                    {
                        "room": "Friedrich LIST",
                        "session": "GACI Parcours Advanced : Traitements percutanés de l’embolie pulmonaire",
                    },
                    {
                        "room": "George STEPHENSON",
                        "session": "Session TUC : Atelier ECG, et si c’était pas la coronaire ?",
                    },
                ],
                "17h45 - 18h45": [
                    {
                        "room": "Louis ARMAND (Plénière)",
                        "session": "GACI Parcours Basic : Les lésions pluritronculaires",
                    },
                    {
                        "room": "Friedrich LIST",
                        "session": "GACI Parcours Advanced : Angioplastie au ballon actif",
                    },
                    {
                        "room": "George STEPHENSON",
                        "session": "GACI Parcours Expert : Réparation tricuspide bord à bord",
                    },
                ],
            }
        ),
    }
)

PAUSE_LABEL = "☕ Pauză / Nu particip"


def option_label(item):
    return f"{item['room']} | {item['session']}"


def init_state():
    for day, slots in CONGRESS_DATA.items():
        for time_range in slots.keys():
            key = f"choice::{day}::{time_range}"
            if key not in st.session_state:
                st.session_state[key] = PAUSE_LABEL


def get_selected_items():
    selected = []

    for day, slots in CONGRESS_DATA.items():
        for time_range, sessions in slots.items():
            key = f"choice::{day}::{time_range}"
            selected_value = st.session_state.get(key, PAUSE_LABEL)

            if selected_value == PAUSE_LABEL:
                continue

            match = None
            for session in sessions:
                if option_label(session) == selected_value:
                    match = session
                    break

            if match is not None:
                selected.append(
                    {
                        "day": day,
                        "time": time_range,
                        "room": match["room"],
                        "session": match["session"],
                    }
                )

    return selected


def render_mobile_card(item):
    st.markdown(
        f"""
        <div style="
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(250,250,250,0.12);
            border-radius: 16px;
            padding: 14px 14px 12px 14px;
            margin-bottom: 10px;
        ">
            <div style="font-size: 0.95rem; opacity: 0.88; margin-bottom: 6px;">
                🗓️ {item['day']} &nbsp;•&nbsp; ⏰ {item['time']}
            </div>
            <div style="font-size: 1.02rem; line-height: 1.45; font-weight: 700;">
                📍 {item['room']}<br>{item['session']}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 5rem;
            max-width: 760px;
        }

        h1, h2, h3 {
            letter-spacing: -0.02em;
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 0.35rem;
            flex-wrap: wrap;
        }

        .stTabs [data-baseweb="tab"] {
            border-radius: 12px;
            padding: 0.55rem 0.9rem;
            height: auto;
        }

        div[data-testid="stSelectbox"] > label {
            font-weight: 700;
        }

        @media (max-width: 640px) {
            .block-container {
                padding-left: 0.9rem;
                padding-right: 0.9rem;
            }

            h1 {
                font-size: 1.65rem !important;
            }

            h2 {
                font-size: 1.25rem !important;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

init_state()

st.title("🩺 Mon assistant congrès")
st.caption("Construis ton itinéraire perso, créneau par créneau.")

with st.container(border=True):
    st.markdown(
        "**📍 Congrès :** Les Rencontres TUC-GACI 2026  \n"
        "**🏛️ Lieu :** UIC-P Espaces Congrès, Paris  \n"
        "**📱 Astuce :** choisis une session à chaque horaire, puis descends voir ton itinéraire final optimisé pour le téléphone."
    )

days = list(CONGRESS_DATA.keys())
tabs = st.tabs([f"📅 {day}" for day in days])

for tab, day in zip(tabs, days):
    with tab:
        st.subheader(day)

        for time_range, sessions in CONGRESS_DATA[day].items():
            st.markdown(f"### ⏰ {time_range}")

            selectable_sessions = [
                s for s in sessions if s["room"] not in ["Pause", "Transition"]
            ]

            if len(selectable_sessions) == 0:
                if sessions[0]["room"] == "Pause":
                    st.info("☕ Pause")
                elif sessions[0]["room"] == "Transition":
                    st.warning("🚶 Transition / changement de salle / Lunch Bags")
                continue

            options = [PAUSE_LABEL] + [option_label(s) for s in selectable_sessions]
            key = f"choice::{day}::{time_range}"
            current_value = st.session_state.get(key, PAUSE_LABEL)

            if current_value in options:
                default_index = options.index(current_value)
            else:
                default_index = 0

            st.selectbox(
                label=f"Choix pour {time_range}",
                options=options,
                index=default_index,
                key=key,
                label_visibility="collapsed",
            )

st.markdown("---")
st.header("🧭 Itinerarul Meu Final")

selected_items = get_selected_items()

if not selected_items:
    st.info(
        "Nicio sesiune selectată încă. Alege din meniurile de mai sus și itinerarul apare automat aici."
    )
else:
    for item in selected_items:
        render_mobile_card(item)

    export_text = "\n\n".join(
        [
            f"{item['day']} | {item['time']}\n{item['room']}\n{item['session']}"
            for item in selected_items
        ]
    )

    st.download_button(
        label="📥 Descarcă itinerarul în format text",
        data=export_text,
        file_name="itinerar_congres_tuc_gaci_2026.txt",
        mime="text/plain",
        use_container_width=True,
    )

with st.expander("🧱 Vezi structura de date Python"):
    st.code(repr(CONGRESS_DATA), language="python")
