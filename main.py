import re
import random
import statistics

from collections import Counter
from bs4 import BeautifulSoup
from database import save_colour_frequencies

HTML_FILE = "python_class_question.html"

def extract_colours_from_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")
    colours = []
    for row in soup.find_all("tr")[1:]:
        cells = row.find_all("td")
        if len(cells) >= 2:
            text = cells[1].get_text(" ", strip=True)
            for colour in re.split(r",\s*", text):
                colour = colour.strip().upper()
                if colour == "BLEW":
                    colour = "BLUE"
                if colour:
                    colours.append(colour)
    return colours

def recursive_search(numbers, target, index=0):
    if index >= len(numbers):
        return -1
    if numbers[index] == target:
        return index
    return recursive_search(numbers, target, index + 1)

def fibonacci_sequence(n):
    result, a, b = [], 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def main():
    colours = extract_colours_from_html(HTML_FILE)
    counts = Counter(colours)
    frequencies = list(counts.values())

    highest = max(frequencies)
    most_worn = [c for c, f in counts.items() if f == highest]

    mean_frequency = statistics.mean(frequencies)
    closest = min(frequencies, key=lambda x: abs(x - mean_frequency))
    mean_colours = [c for c, f in counts.items() if f == closest]

    median_frequency = statistics.median(frequencies)
    median_colours = [c for c, f in counts.items() if f == median_frequency]

    variance = statistics.pvariance(frequencies)
    red_count = counts.get("RED", 0)
    red_probability = red_count / len(colours)

    print("=" * 60)
    print("BINCOM PYTHON BASIC DEVELOPER TEST")
    print("=" * 60)
    print(f"\nTotal colour entries: {len(colours)}")

    print("\nCOLOUR FREQUENCIES")
    print("-" * 30)
    for colour, frequency in counts.most_common():
        print(f"{colour:<10} : {frequency}")

    print("\n1. COLOUR MOSTLY WORN")
    print(f"Colour(s): {', '.join(most_worn)}")
    print(f"Frequency: {highest}")

    print("\n2. MEAN COLOUR")
    print(f"Mean frequency: {mean_frequency:.2f}")
    print(f"Colour(s) closest to mean: {', '.join(mean_colours)}")

    print("\n3. MEDIAN COLOUR")
    print(f"Median frequency: {median_frequency}")
    print(f"Colour(s): {', '.join(median_colours)}")

    print("\n4. POPULATION VARIANCE")
    print(f"{variance:.4f}")

    print("\n5. PROBABILITY OF RED")
    print(f"{red_count}/{len(colours)} = {red_probability:.4f} ({red_probability * 100:.2f}%)")

    print("\n6. POSTGRESQL")
    try:
        save_colour_frequencies(dict(counts))
        print("Colour frequencies saved successfully.")
    except Exception as error:
        print("Database save was not completed.")
        print(f"Reason: {error}")

    print("\n7. RECURSIVE SEARCH")
    numbers = [10, 20, 30, 40, 50]
    print("Example list:", numbers)
    value = input("Enter a number to search for (or press Enter to skip): ").strip()
    if value:
        try:
            target = int(value)
            index = recursive_search(numbers, target)
            print(f"{target} found at index {index}." if index != -1 else f"{target} was not found.")
        except ValueError:
            print("Invalid number.")

    print("\n8. RANDOM 4-DIGIT BINARY")
    binary = "".join(random.choice("01") for _ in range(4))
    print(f"Binary: {binary}")
    print(f"Base 10: {int(binary, 2)}")

    print("\n9. FIRST 50 FIBONACCI NUMBERS")
    fib = fibonacci_sequence(50)
    print(fib)
    print(f"Sum: {sum(fib)}")

if __name__ == "__main__":
    main()
