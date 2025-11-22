import streamlit as st
import pandas as pd
import datetime

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Brown Brothers Bohol Trip",
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- SIDEBAR ---
st.sidebar.title("🌴 Bohol 2025")
st.sidebar.write("Dec 26 - Jan 6")
page = st.sidebar.radio("Go to", ["Itinerary Overview", "The Wingman's Guide", "Flight Info", "Base Camp & Wifi"])

# --- DATA: ITINERARY ---
data = [
    {"Date": "Dec 26", "Day": "Friday", "Activity": "Depart Seattle (SEA)", "Time": "9:30 PM", "Notes": "Long haul to Manila"},
    {"Date": "Dec 28", "Day": "Sunday", "Activity": "Arrive Panglao (TAG)", "Time": "1:20 PM", "Notes": "Land, check into Airbnb"},
    {"Date": "Dec 29", "Day": "Monday", "Activity": "Chill & Acclimatize", "Time": "All Day", "Notes": "Sardine run snorkeling (Napaling)"},
    {"Date": "Dec 30", "Day": "Tuesday", "Activity": "The Big Adventure", "Time": "5:00 AM", "Notes": "Alicia Panoramic Park (The Ridge Run)"},
    {"Date": "Jan 1", "Day": "Thursday", "Activity": "New Year's Recovery", "Time": "AM", "Notes": "Slow breakfast @ Airbnb"},
    {"Date": "Jan 6", "Day": "Tuesday", "Activity": "Fly Home", "Time": "11:00 AM", "Notes": "Panglao -> Manila -> Vancouver -> SEA"}
]
df = pd.DataFrame(data)

# --- PAGE 1: OVERVIEW ---
if page == "Itinerary Overview":
    st.title("🌴 The Bohol Expedition")
    st.caption("Operation: Meet the Parents & Dive Deep")
    
    # Metric Cards
    col1, col2, col3 = st.columns(3)
    # Dynamic countdown
    days_left = (datetime.date(2025, 12, 26) - datetime.date.today()).days
    col1.metric("Days Until Launch", f"{days_left} days")
    col2.metric("Location", "Panglao, Bohol")
    col3.metric("Crew", "Brown Brothers + 1")

    st.divider()
    
    # Timeline
    st.subheader("📅 The Schedule")
    st.dataframe(
        df, 
        column_config={
            "Date": st.column_config.TextColumn("Date", width="small"),
            "Activity": st.column_config.TextColumn("Main Event", width="large"),
            "Notes": st.column_config.TextColumn("Details", width="medium"),
        },
        hide_index=True,
        use_container_width=True
    )

# --- PAGE 2: WINGMAN GUIDE ---
elif page == "The Wingman's Guide":
    st.title("🕵️ The Wingman Protocols")
    st.info("Confidential: For the Couch Surfer's Eyes Only")
    
    tab1, tab2, tab3 = st.tabs(["🎁 Gifts (Pasalubong)", "🏃‍♂️ Solo Missions", "🤝 Etiquette"])
    
    with tab1:
        st.write("### The Peace Offerings")
        st.success("✅ **Titas:** Bath & Body Works, Chocolates (Ferrero)")
        st.success("✅ **Titos:** Duty Free Whisky, Baseball Caps")
        st.warning("⚠️ **Rule:** Do not let Brother pay for everything.")

    with tab2:
        st.write("### Escape Routes")
        st.markdown("""
        * **Napaling Reef:** 5 min walk. Snorkel with Sardines.
        * **North Zen Villas:** Bamboo walk for sunset.
        * **Alicia Park:** 5km Ridge Run (Day trip).
        """)

    with tab3:
        st.write("### Cultural Cheat Sheet")
        st.markdown("""
        * **'Mano Po':** Hand to forehead greeting for elders.
        * **'Kain Tayo':** (Let's eat) - always accept a small bite.
        * **Tsinelas:** Take your shoes/slippers off at the door.
        """)

# --- PAGE 3: FLIGHTS ---
elif page == "Flight Info":
    st.title("✈️ Flight Logistics")
    
    # SECRETS USED HERE
    try:
        st.metric("Booking Reference", st.secrets["flight_ref"])
    except:
        st.warning("Secrets not configured yet")

    st.markdown("""
    **Outbound (Dec 26-28)**
    * SEA -> MNL (14h 35m)
    * *Layover MNL (4h 45m)*
    * MNL -> DVO (1h 55m)
    * DVO -> TAG (1h)
    
    **Return (Jan 6)**
    * TAG -> MNL (11:00 AM)
    * *Layover MNL (7h 50m)*
    * MNL -> YVR -> SEA
    """)

# --- PAGE 4: BASE CAMP (SECRETS HEAVY) ---
elif page == "Base Camp & Wifi":
    st.title("📍 Base Camp Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏠 Address")
        # SECRETS USED HERE
        try:
            st.success(st.secrets["airbnb_address"])
            st.write(f"**Door Code:** {st.secrets['door_code']}")
        except:
            st.error("Add secrets to view address")
            
    with col2:
        st.subheader("📶 Wifi")
        # SECRETS USED HERE
        try:
            st.code(f"Network: {st.secrets['wifi_ssid']}\nPass: {st.secrets['wifi_pass']}")
        except:
            st.error("Add secrets to view wifi")

    st.subheader("🗺️ Map")
    # Coordinates for Napaling Reef (Approx)
    map_data = pd.DataFrame({'lat': [9.6047], 'lon': [123.7667]})
    st.map(map_data, zoom=14)
