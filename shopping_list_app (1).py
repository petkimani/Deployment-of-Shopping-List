import streamlit as st

# Initialize shopping dictionary in session state
if 'shopping_dict' not in st.session_state:
    st.session_state.shopping_dict = {}

def add_item(item, quantity):
    if item.strip() == "":
        return "Item name cannot be empty."
    if not quantity.isdigit() or int(quantity) < 1:
        return "Quantity must be a positive integer."

    quantity = int(quantity)
    if item in st.session_state.shopping_dict:
        st.session_state.shopping_dict[item] += quantity
        return f"{quantity} {item}(s) added."
    else:
        st.session_state.shopping_dict[item] = quantity
        return f"{item} added."

def remove_item(item, quantity):
    if not st.session_state.shopping_dict:
        return "List is empty."
    if item not in st.session_state.shopping_dict:
        return "Item not found."
    if not quantity.isdigit() or int(quantity) < 1:
        return "Quantity must be a positive integer."

    quantity = int(quantity)
    if quantity >= st.session_state.shopping_dict[item]:
        del st.session_state.shopping_dict[item]
        return f"All {item} removed."
    else:
        st.session_state.shopping_dict[item] -= quantity
        return f"{quantity} {item} removed."

def view_list():
    if st.session_state.shopping_dict:
        return "\n".join([f"{item}: {quantity}" for item, quantity in st.session_state.shopping_dict.items()])
    return "List is empty."

# Streamlit app
st.title("Shopping List Manager")

choice = st.selectbox("Menu", ["Add Item", "Remove Item", "View List"])

if choice == "Add Item":
    if len(st.session_state.shopping_dict) < 7:
        item = st.text_input("Item to add")
        quantity = st.text_input("Quantity", "1")
        if st.button("Add"):
            result = add_item(item, quantity)
            st.write(result)
    else:
        st.write("List is full (max 7 items).")

elif choice == "Remove Item":
    item = st.text_input("Item to remove")
    quantity = st.text_input("Quantity", "1")
    if st.button("Remove"):
        result = remove_item(item, quantity)
        st.write(result)

elif choice == "View List":
    st.text(view_list())

if st.button("Quit"):
    st.write("Goodbye!")
    st.session_state.shopping_dict.clear()
