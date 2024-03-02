# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import streamlit as st
import pandas as pd
import numpy as np

# +
# Set page to wide mode
st.set_page_config(layout="wide")




# +
st.title("Streamlit 101")
st.markdown("\n")

title = st.text_input('Question', 'Ask a question...')
st.markdown("\n")
st.markdown("\n")

# -

table1 = """| Comparison Factors | Kinesis Freestyle2      | Logitech Ergo K860      | Microsoft Sculpt        | Logitech K350      | Perixx Periboard-512    | Cloud Nine ErgoTKL      | Kinesis Freestyle Edge RGB | Keychron Q11          |
| ----------------- | ----------------------- | ----------------------- | ----------------------- | ------------------ | ----------------------- | ----------------------- | -------------------------- | --------------------- |
| Price             | $134 at Amazon          | $126 at Amazon          | $330 at Amazon          | $36 at Best Buy    | $50 at Amazon           | $179.99 at Amazon       | $199 at Amazon             | $224.99 at Amazon     |
| Type              | Split                   | Curved unibody          | Curved unibody          | Wave unibody       | Split                   | Split                   | Split mechanical           | Split                 |
| Connection        | Wired                   | Wireless, wired         | Wireless                | Wireless           | Wired                   | Wired                   | Wired                      | Wired                 |
| Power             | USB                     | 2 AA batteries          | 3 lithium-ion batteries | 2 AAA batteries    | Cable                   | Via cable               | Via cable                  | Via cable             |
| Extra Features    | None                    | Adjustable legs,        | Separate number pad     | Customizable keys  | Laser-printed keys,     | RGB lighting, USB       | RGB per-key lighting       | Hot-swappable key     |
|                   |                         | built-in wrist rest     |                         |                    | multimedia keys         | passthrough             |                            | switches              |
| Pros              | Extremely comfortable,  | Smooth keys, adjustable | Elegant look,           | Lots of extra      | Comfortable, multimedia | Comfortable, bright     | True Cherry MX switches,   | Attractive design,    |
|                   | adjustable shape        | wrist position for      | comfortable, separate   | customizable keys  | keys                    | lighting, mechanical    | ergonomic design           | programmable keys     |
|                   |                         | different heights       | number pad              |                    |                         | key switches            |                            |                       |
| Cons              | No lighting, not        | Wrist rest is attached; | Shallow keys            | Feels cheaply made | Takes up a lot of desk  | Split design takes some | Steep learning curve,      | Expensive, no angled  |
|                   | particularly attractive | if fabric wears, you’re |                         |                    | space                   | getting used to,        | optional lift kit costs    | feet, wrist rest sold |
|                   |                         | out of luck             |                         |                    |                         | Windows-only software   | extra                      | separately            |"""

table2 = """| Comparison Factors            | ZSA Voyager                | Kinesis Freestyle2                 | Logitech Ergo K860              | Microsoft Sculpt                 | Perixx Periboard-512           |
|-------------------------------|----------------------------|-----------------------------------|---------------------------------|---------------------------------|--------------------------------|
| **Price**                     | Around $365                | $89 - $134                        | $119 - $126                     | $60 - $330                      | Around $36                     |
| **Type**                      | Ergonomic Mechanical Split Keyboard | Ergonomic Split Keyboard          | Ergonomic Keyboard               | Ergonomic Split Keyboard        | Ergonomic Split Keyboard       |
| **Design**                    | Low-profile, split, highly customizable, laptop-friendly | Split design with up to 9 or 20 inches separation, Windows layout | Long typing sessions, built-in wrist rest, varied tilt legs | Comfortable typing, cushioned palm rest, domed shape to reduce wrist pronation | Inexpensive split design, supports varied finger lengths, wave design |
| **Key Layout**                | 52-key compact layout, columnar layout for ease of reach | Standard layout with VIP3 lifters for tenting | Standard layout with integrated palm rest | Cushioned palm rest, separate number pad included | Wave design, supports varied finger lengths |
| **Customization**             | Oryx software for key remapping, choice of keycaps and Kailh Choc switches, LED lighting | VIP3 lifters for adjustable angles and comfort | Adjustable tilt legs, smooth keys | Elegant look, comfortable form | Customizable keys, multimedia keys |
| **Portability**               | Designed for portability, slim form factor | Not specifically designed for portability | Not specifically designed for portability | Not specifically designed for portability | Not specifically designed for portability |
| **Accessories**               | Carrying case, extra keycaps, USB-C cables, USB-C to USB-A dongle, TRRS headphone cable | N/A                                   | N/A                                   | Separate number pad as a bonus accessory | Multimedia keys at the top      |
| **Warranty**                  | Two-year warranty          | Variable based on retailer        | Variable based on retailer      | Variable based on retailer      | Variable based on retailer      |
| **Ergonomic Features**        | Reduces muscle strain, customizable tenting legs | Split design allows for natural arm and hand position | Built-in wrist rest, adjustable position | Domed shape reduces wrist pronation, cushioned palm rest | Wave design mimics natural finger length |
| **Connection**                | USB-C                      | Wired USB                         | Wireless and wired, 2 AA batteries | Wireless, 3 lithium-ion batteries | Wired                         |
| **Availability**              | Direct purchase from ZSA, ships in approx. three weeks | Available on various retailers such as Amazon | Available on various retailers such as Amazon, Walmart, B&H Photo | Available on various retailers such as Amazon, B&H Photo, QVC | Available on various retailers such as Best Buy, Walmart, B&H Photo |
| **Customizable Lighting**     | Per-key RGB LED lighting    | None                              | None                              | None                              | None                           |
| **Market Focus**              | Global with direct shipping policies | Global, depending on shipping policies | Global, depending on shipping policies | Global, depending on shipping policies | Global, depending on shipping policies |
| **Key Switches**              | Four low-profile mechanical switch types offered | Membrane switches compatible with low-force keys | Mechanical switches | Membrane switches | Mechanical switches            |
| **Travel Compatibility**      | Specifically designed for travel with a laptop | Can be adapted with separable halves | Not specifically designed for travel | Not specifically designed for travel | Not specifically designed for travel |
| **OS Compatibility**          | Mac, Windows, Linux         | Mac, Windows                      | Mac, Windows                     | Windows                           | Most operating systems         |
| **Community and Support**     | Active community, layout tours, robust support | Robust support and community resources | Well-known brand with strong support | Well-known brand with strong support | Known for its budget value and support |
| **Overall Value Proposition** | Premium product aimed at reducing repetitive strain, customizable for niche audience | Balance between customization and price for ergonomic benefit | Value for those requiring long session comfort | Business-oriented with aesthetic design | Budget-friendly split keyboard option |
| **Hot Swappable Switches**    | Yes                         | No                                | No                                | No                                | No                             |
| **Open Source Firmware**      | Yes, supports QMK           | Yes, supports QMK                 | No                                | No                                | No                             |
| **Tenting Capabilities**      | Yes, with magnetic tenting legs | Yes, with VIP3 lifters            | Yes, fixed tilt, integrated wrist rest | Yes, domed design provides natural tenting | No                             |
| **Material**                  | Low-profile with steel backplate, high-quality plastic | High-quality plastic with optional tenting lifters | High-quality plastic with integrated palm rest | High-quality plastic with cushioned palm rest | High-quality plastic          |
| **Ortholinear**               | Yes, columnar layout       | No                                | No                                | No                                | No                             |
| **Cylindrical Keycap Profile** | Not specified              | Yes                               | Yes                               | Yes                               | Yes                            |
"""


def markdown_to_dataframe(markdown):
    # Split the table into lines
    lines = markdown.strip().split("\n")
    # Extract the headers
    headers = [header.strip() for header in lines[0].split("|")[1:-1]]
    # Initialize a list to hold the row data
    rows = []

    # Process each row in the Markdown table
    for line in lines[2:]:
        # Extract the cells from the current row
        cells = [cell.strip() for cell in line.split("|")[1:-1]]
        # Append the cells to the rows list as a tuple
        rows.append(cells)
    
    # Convert the list of tuples into a DataFrame
    df = pd.DataFrame(rows, columns=headers)
    return df



# + active=""
# def markdown_to_dataframe(markdown):
#     
#     # Split the markdown table into lines
#     lines = markdown.strip().split('\n')
#     
#     # Extract column names
#     columns = [col.strip() for col in lines[0].split('|') if col.strip()]
#     
#     # Prepare a list to hold row data
#     data = []
#     
#     # Process each row in the markdown table
#     for line in lines[2:]:  # Skip the header and separator lines
#         # Split the line by "|" to get individual cell values
#         cells = [cell.strip() for cell in line.split('|') if cell.strip()]
#         # Append the cells to the data list
#         data.append(cells)
#     
#     # Create a DataFrame from the processed data
#     df_correct = pd.DataFrame(data, columns=columns)
#     
#     return df_correct

# +
df1 = markdown_to_dataframe(table1)
df2 = df1.set_index('Comparison Factors', drop=True)

# Apply styling (e.g., set column width)
#styled_df = df1.style.set_properties(**{'height': '900px', 'text-align': 'left'})

# Estimate height: number_of_rows * pixel_height_per_row + a small margin
estimated_height = len(df2) * 35 + 40  # Adjust 25 based on your row height

st.dataframe(df2, height=estimated_height)
# -


