import re

def analyze_component(filepath):
    with open(filepath, "r") as file:
        code = file.read()

    # Component name from filename
    component_name = filepath.split("/")[-1].replace(".jsx", "")

    # --- Extract props defined via PropTypes ---
    props_shape_match = re.search(r"user:\s*PropTypes\.shape\(\{([^}]+)\}\)", code)
    props_received = 0
    if props_shape_match:
        shape_block = props_shape_match.group(1)
        props_received = len(re.findall(r":\s*PropTypes\.", shape_block))

    # --- Extract props used in the component (e.g., user.name, user.email) ---
    used_props = set(re.findall(r"user\.(\w+)", code))
    props_used = len(used_props)

    # --- Detect memoization ---
    is_memoized = "export default memo(" in code or "React.memo(" in code

    # --- Build AI input object ---
    component_info = {
        "component": component_name,
        "actualDuration": 0.5,     # Assumed default
        "renderTime": 20.0,        # Assumed default
        "stateUpdates": 2,         # Assumed default
        "propsReceived": props_received,
        "propsUsed": props_used,
        "isMemoized": is_memoized
    }

    return [component_info]
