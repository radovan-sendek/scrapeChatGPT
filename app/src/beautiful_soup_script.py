import os
import re
from bs4 import BeautifulSoup, NavigableString


def scrape(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find active tab caption
    active_tab = soup.find('a', class_='flex items-center gap-2 rounded-lg p-2 bg-token-surface-primary')
    active_tab_caption = active_tab.find('div', class_='relative grow overflow-hidden whitespace-nowrap').get_text(strip=True)

    # Find the divs that hold the question and change their class from class="" to class="question"
    user_question_outer_divs = soup.find_all('div', {'data-message-author-role': 'user'})
    for user_div in user_question_outer_divs:
        question_div = user_div.find('div', class_='')
        if question_div:
            question_div['class'] = "question"

    # Find all divs with questions and answers
    divs = soup.find_all(has_exact_class)
    # Add '####' and a new line to create a heading (obsidian format)
    for div in divs:
        if div.get('class') == ['']:
            div.string = '\n#### ' + div.get_text() + '\n'
    # Get all child elements from divs into a one string
    div_nested_elements = []
    for div in divs:
        div_nested_elements.append("".join(str(child) for child in div.children))
    result = "".join(div_nested_elements)
    # Parse the content again
    soup = BeautifulSoup(result, 'html.parser')
    # Get rid of all buttons, pre and span tags
    for button in soup.find_all('button'):
        button.decompose()
    for tag in soup.find_all(['pre', 'span']):
        tag.unwrap()
    # Add ``` and the name of the language for code formatting
    for code_tag in soup.find_all('code'):
        if 'class' in code_tag.attrs:
            language_classes = [i for i in code_tag['class'] if i.startswith('language-')]
            if language_classes:
                language = language_classes[0].replace('language-', '')
                new_content = NavigableString(f"\n```{language}\n//start code\n {code_tag.get_text()}\n```\n")
                code_tag.replace_with(new_content)
    # Unwrap content from different elements
    for tag in soup.find_all(['p', 'ul', 'ol', 'li', 'div']):
        tag.insert_before(NavigableString('\n'))
        tag.unwrap()

    finished_content = str(soup)
    create_obsidian_file(finished_content, active_tab_caption)


# Class 'question' is for the question (was "", but in code above we change it to "question",
# the other one is for the answer
def has_exact_class(tag):
    return (
        tag.name == 'div'
        and tag.has_attr('class')
        and (
            'question' in tag['class']
            or {'markdown', 'prose', 'w-full', 'break-words', 'dark:prose-invert', 'dark'}.issubset(tag['class'])
        )
    )


def sanitize_filename(filename):
    filename = filename.replace(" ", "_")
    # Remove or replace special characters
    filename = re.sub(r'[\\/:*?"<>|]', '_', filename)

    return filename


def create_obsidian_file(content, name):
    folder_name = "obsidian_files"
    sanitized_name = sanitize_filename(name)
    file_name = f"{sanitized_name}.md"

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Path to the new file
    file_path = os.path.join(folder_name, file_name)

    # Write content to the file
    with open(file_path, "w", encoding='utf-8') as file:
        file.write(content)
