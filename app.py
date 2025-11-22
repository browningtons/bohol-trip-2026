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
st.sidebar.title("🌴 Bohol 2026")
st.sidebar.caption("Dec 26 - Jan 6")
page = st.sidebar.radio("Go to", ["Itinerary Overview", "The Wingman's Guide", "Flight Info", "Base Camp & Wifi"])

# --- DATA: ITINERARY (Enriched with PDF Details) ---
data = [
    {"Date": "Dec 26", "Day": "Fri", "Activity": "Depart Seattle (SEA)", "Time": "9:30 PM", "Notes": "Flight PR125 - 14.5h Long Haul"},
    {"Date": "Dec 28", "Day": "Sun", "Activity": "Arrival Gauntlet", "Time": "1:20 PM", "Notes": "Land TAG via MNL & DVO. Check into Napaling Airbnb."},
    {"Date": "Dec 29", "Day": "Mon", "Activity": "The Backyard & Chill", "Time": "All Day", "Notes": "Napaling Sardine Run (No boat needed - stairs at cliff). Dinner @ Ubeco?"},
    {"Date": "Dec 30", "Day": "Tue", "Activity": "The Big Three", "Time": "8:00 AM", "Notes": "Chocolate Hills (ATV), Tarsier Sanctuary (Corella), Loboc River Cruise"},
    {"Date": "Dec 31", "Day": "Wed", "Activity": "Island Hopping", "Time": "6:00 AM", "Notes": "Balicasag (Turtles) & Virgin Island (Sea Urchin/Banana)."},
    {"Date": "Jan 2", "Day": "Fri", "Activity": "The Champion Run", "Time": "4:00 AM", "Notes": "Alicia Panoramic Park (The Ridge Run) or Lamanoc Island (Mystical Caves)."},
    {"Date": "Jan 6", "Day": "Tue", "Activity": "Fly Home", "Time": "11:00 AM", "Notes": "Flight PR2774 -> MNL Layover -> Flight PR116 -> YVR -> SEA"}
]
df = pd.DataFrame(data)

# --- PAGE 1: OVERVIEW ---
if page == "Itinerary Overview":
    st.title("🌴 The Bohol Expedition 2026")
    st.caption("Operation: Meet the Parents & Dive Deep")
    
    # Metric Cards
    col1, col2, col3 = st.columns(3)
    # Dynamic countdown
    days_left = (datetime.date(2025, 12, 26) - datetime.date.today()).days
    col1.metric("Days Until Launch", f"{days_left} days")
    col2.metric("Location", "Panglao, Bohol", "Amihan Season (Cool/Breezy)")
    col3.metric("Crew", "Brown Brothers + 1")

    st.divider()
    
    # Timeline
    st.subheader("📅 The Master Schedule")
    st.dataframe(
        df, 
        column_config={
            "Date": st.column_config.TextColumn("Date", width="small"),
            "Activity": st.column_config.TextColumn("Main Event", width="large"),
            "Notes": st.column_config.TextColumn("Intel", width="large"),
        },
        hide_index=True,
        use_container_width=True
    )
    
    st.divider()
    st.info("💡 **Pro Tip:** Cash is King. Get PHP at the airport ATM. Download the 'Grab' app for transport.")

# --- PAGE 2: WINGMAN GUIDE ---
elif page == "The Wingman's Guide":
    st.title("🕵️ The Wingman Protocols")
    st.info("Confidential: For the Couch Surfer's Eyes Only")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🎁 Gifts (Pasalubong)", "🏃‍♂️ Solo Missions", "🤝 Etiquette", "🍔 Food"])
    
    with tab1:
        st.write("### The Peace Offerings")
        st.markdown("""
        * **For Titas (Aunts/Moms):** Bath & Body Works lotions/soaps, perfumes, specific chocolates (Ferrero Rocher).
        * **For Titos (Uncles/Dads):** Duty Free Whisky, branded baseball caps.
        """)
        st.warning("⚠️ **Golden Rule:** If there is a family dinner, do not let Brother pay for *everything*. Offer to bring dessert (e.g., Cake from Bohol Bee Farm).")

    with tab2:
        st.write("### Escape Routes (When they need space)")
        col1, col2 = st.columns(2)
        with col1:
            st.write("#### 🧘‍♂️ Chill / Zen")
            st.write("**Napaling Reef:** Snorkel with the Sardine ball (stairs at cliff, no boat needed).")
            st.write("**North Zen Villas:** Bamboo boardwalk for sunset (Day Pass available).")
            st.write("**Jing Yoga:** Drop-in classes near Alona Beach.")
        with col2:
            st.write("#### 🌋 Adventure")
            st.write("**Alicia Panoramic Park:** 'The Ridge Run'. Steep, technical loop (Binabaje Hills).")
            st.write("**Lamanoc Island:** The 'Mystical' option. Red hematite paintings & shaman caves.")

    with tab3:
        st.write("### Cultural Cheat Sheet")
        st.markdown("""
        * **'Mano Po':** Traditional greeting for elders (hand to forehead). Shows massive respect.
        * **'Kain Tayo':** (Let's eat) - You will be fed a lot. Always accept at least a small bite.
        * **Titles:** Use 'Tito' (Uncle) and 'Tita' (Auntie) once introduced.
        """)

    with tab4:
        st.write("### Dining Near Napaling")
        st.write("* **Ubeco:** Highly rated fusion/comfort food.")
        st.write("* **Barwoo:** Popular Korean bistro.")
        st.write("* **Mist:** Jungle cafe vibe (Coffee/Cocktails).")

# --- PAGE 3: FLIGHTS ---
elif page == "Flight Info":
    st.title("✈️ Flight Logistics")
    
    # Flight Reference Secret
    try:
        st.metric("Booking Reference", st.secrets["flight_ref"])
    except:
        st.warning("Add 'flight_ref' to secrets.toml")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🛫 Outbound (Dec 26-28)")
        st.write("**SEA -> MNL** | PR125 | 14h 35m")
        st.write("*Layover: 4h 45m (Stay in airport!)*")
        st.write("**MNL -> DVO** | PR2813 | 1h 55m")
        st.error("⚠️ **Davao Stop:** 1h 35m Short Connection. Don't stop for coffee!")
        st.write("**DVO -> TAG** | PR2372 | 1h")

    with col2:
        st.subheader("🛬 Return (Jan 6)")
        st.write("**TAG -> MNL** | PR2774 | 11:00 AM")
        st.error("⚠️ **Manila Layover:** 7h 50m ('Danger Zone'). Go to Newport World Resorts via Runway Manila bridge.")
        st.write("**MNL -> YVR** | PR116 | 11h 35m")
        st.write("**YVR -> SEA** | AS2122 | 1h 6m")

# --- PAGE 4: BASE CAMP ---
elif page == "Base Camp & Wifi":
    st.title("📍 Napaling Base Camp")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏠 Address")
        try:
            st.success(st.secrets["airbnb_address"])
            st.write(f"**Door Code:** {st.secrets['door_code']}")
        except:
            st.info("Deploy to see secrets")
            
    with col2:
        st.subheader("📶 Wifi")
        try:
            st.code(f"Network: {st.secrets['wifi_ssid']}\nPass: {st.secrets['wifi_pass']}")
        except:
            st.info("Deploy to see secrets")

    st.subheader("🗺️ Map")
    # Coordinates for Napaling Reef
    map_data = pd.DataFrame({'lat': [9.6047], 'lon': [123.7667]})
    st.map(map_data, zoom=14)
