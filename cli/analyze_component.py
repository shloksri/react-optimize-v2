import re

def analyze_component(filepath):
    with open(filepath, "r") as file:
        code = file.read()

    # --- Extract component name from filename ---
    component_name = filepath.split("/")[-1].replace(".jsx", "")

    # --- Step 1: Extract prop variable name (e.g., 'user' or 'stats') ---
    prop_var_match = re.search(r"const\s+\w+\s*=\s*\(\{\s*(\w+)\s*\}\)", code)
    prop_var = prop_var_match.group(1) if prop_var_match else "user"

    # --- Step 2: Find PropTypes.shape definition for that prop_var ---
    prop_shape_regex = re.compile(
        rf"{component_name}\.propTypes\s*=\s*\{{[^{{}}]*{prop_var}:\s*PropTypes\.shape\(\{{(.*?)\}}\)",
        re.DOTALL,
    )
    shape_match = prop_shape_regex.search(code)
    props_received = 0
    if shape_match:
        shape_body = shape_match.group(1)
        props_received = len(re.findall(r":\s*PropTypes\.", shape_body))

    # --- Step 3: Count prop usage in JSX (e.g., stats.visits) ---
    used_props = set(re.findall(rf"{prop_var}\.(\w+)", code))
    props_used = len(used_props)

    # --- Step 4: Check for memoization ---
    is_memoized = "export default memo(" in code or "React.memo(" in code

    # --- Step 5: Build AI input object ---
    component_info = {
        "component": component_name,
        "actualDuration": 0.3,
        "renderTime": 12.0,
        "stateUpdates": 0,
        "propsReceived": props_received,
        "propsUsed": props_used,
        "isMemoized": is_memoized,
    }

    return [component_info]
