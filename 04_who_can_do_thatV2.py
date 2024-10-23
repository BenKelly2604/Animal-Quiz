import tkinter as tk
from PIL import Image, ImageTk
import random
import textwrap

# Initialize global variables
window_stack = []

# List of animals sorted alphabetically
animal_list = sorted(["Alpaca", "Ant", "Bat", "Bee", "Crocodile", "Deer", "Cheetah", "Duck",
                      "Crab", "Spider", "Rhino", "Cat", "Dog", "Giraffe", "Bear", "Elephant", "Tiger",
                      "Lion", "Zebra", "Kangaroo", "Buffalo", "Beaver", "Donkey", "Tasmanian Devil", "Hamster", "Hawk",
                      "Fox", "Hedgehog", "Horse", "Kiwi", "Lizard", "Leopard", "Koala", "Lemur", "Mole", "Panther",
                      "Pig", "Penguin", "Platypus", "Pelican", "Orangutan", "Polar Bear", "Rabbit", "Sloth", "Seagull",
                      "Red Panda", "Snake", "Sheep", "Squirrel", "Turkey", "Wolf", "Wombat"])

# Define question lists for different difficulty levels
easy_questions = [
    {"question": "Which animal is known for its soft wool and is often found on farms?", "options": ["Alpaca", "Ant", "Bat", "Bee"], "answer": "Alpaca"},
    {"question": "Which insect is known for building anthills?", "options": ["Ant", "Bee", "Spider", "Crab"], "answer": "Ant"},
    {"question": "Which mammal is capable of sustained flight?", "options": ["Bat", "Duck", "Penguin", "Ostrich"], "answer": "Bat"},
    {"question": "Which insect is known for producing honey?", "options": ["Bee", "Ant", "Butterfly", "Fly"], "answer": "Bee"},
    {"question": "Which large reptile is known for living in rivers and having powerful jaws?", "options": ["Crocodile", "Alligator", "Komodo Dragon", "Gharial"], "answer": "Crocodile"},
    {"question": "Which animal is known for having antlers?", "options": ["Deer", "Rabbit", "Kangaroo", "Elephant"], "answer": "Deer"},
    {"question": "Which animal is known as the fastest land animal?", "options": ["Cheetah", "Lion", "Tiger", "Elephant"], "answer": "Cheetah"},
    {"question": "Which bird is often seen swimming in ponds and lakes?", "options": ["Duck", "Penguin", "Swan", "Goose"], "answer": "Duck"},
    {"question": "Which crustacean is known for its pincers and lives in the ocean?", "options": ["Crab", "Lobster", "Shrimp", "Jellyfish"], "answer": "Crab"},
    {"question": "Which arachnid is known for spinning webs?", "options": ["Spider", "Scorpion", "Tick", "Mite"], "answer": "Spider"},
    {"question": "Which large animal has one or two horns on its snout?", "options": ["Rhino", "Elephant", "Lion", "Giraffe"], "answer": "Rhino"},
    {"question": "Which small, carnivorous mammal is often kept as a pet?", "options": ["Cat", "Dog", "Rabbit", "Hamster"], "answer": "Cat"},
    {"question": "Which domesticated mammal is known as man's best friend?", "options": ["Dog", "Cat", "Horse", "Rabbit"], "answer": "Dog"},
    {"question": "Which animal is the tallest land animal?", "options": ["Giraffe", "Elephant", "Lion", "Kangaroo"], "answer": "Giraffe"},
    {"question": "Which large mammal is known for hibernating during the winter?", "options": ["Bear", "Rabbit", "Deer", "Fox"], "answer": "Bear"},
    {"question": "Which large mammal has a trunk?", "options": ["Elephant", "Lion", "Tiger", "Rhino"], "answer": "Elephant"},
    {"question": "Which large feline is known for its stripes?", "options": ["Tiger", "Lion", "Cheetah", "Leopard"], "answer": "Tiger"},
    {"question": "Which large feline is known as the king of the jungle?", "options": ["Lion", "Tiger", "Panther", "Cheetah"], "answer": "Lion"},
    {"question": "Which striped animal is known for living in Africa?", "options": ["Zebra", "Giraffe", "Lion", "Elephant"], "answer": "Zebra"},
    {"question": "Which animal is known for its powerful hind legs and pouches for carrying young?", "options": ["Kangaroo", "Koala", "Wombat", "Rabbit"], "answer": "Kangaroo"},
    {"question": "Which large mammal is known for its curved horns and strong build?", "options": ["Buffalo", "Elephant", "Rhino", "Bear"], "answer": "Buffalo"},
    {"question": "Which animal is known for building dams?", "options": ["Beaver", "Duck", "Otter", "Rabbit"], "answer": "Beaver"},
    {"question": "Which animal is known for its long ears and is often used as a working animal?", "options": ["Donkey", "Horse", "Dog", "Deer"], "answer": "Donkey"},
    {"question": "Which carnivorous marsupial is native to Tasmania?", "options": ["Tasmanian Devil", "Kangaroo", "Koala", "Wombat"], "answer": "Tasmanian Devil"},
    {"question": "Which small rodent is often kept as a pet and known for its cheek pouches?", "options": ["Hamster", "Rabbit", "Mouse", "Squirrel"], "answer": "Hamster"},
    {"question": "Which bird of prey is known for its keen eyesight?", "options": ["Hawk", "Eagle", "Owl", "Falcon"], "answer": "Hawk"},
    {"question": "Which small, carnivorous mammal is known for its cunning nature?", "options": ["Fox", "Wolf", "Bear", "Lion"], "answer": "Fox"},
    {"question": "Which small mammal is known for its spines?", "options": ["Hedgehog", "Porcupine", "Rabbit", "Squirrel"], "answer": "Hedgehog"},
    {"question": "Which large domesticated mammal is often used for riding and racing?", "options": ["Horse", "Donkey", "Buffalo", "Elephant"], "answer": "Horse"},
    {"question": "Which small, flightless bird is native to New Zealand?", "options": ["Kiwi", "Penguin", "Emu", "Ostrich"], "answer": "Kiwi"},
    {"question": "Which reptile is known for its ability to regenerate its tail?", "options": ["Lizard", "Snake", "Crocodile", "Turtle"], "answer": "Lizard"},
    {"question": "Which large feline is known for its distinctive spots?", "options": ["Leopard", "Tiger", "Cheetah", "Lion"], "answer": "Leopard"},
    {"question": "Which marsupial is known for eating eucalyptus leaves?", "options": ["Koala", "Kangaroo", "Wombat", "Tasmanian Devil"], "answer": "Koala"},
    {"question": "Which small primate is known for its large, reflective eyes?", "options": ["Lemur", "Monkey", "Orangutan", "Gibbon"], "answer": "Lemur"},
    {"question": "Which small mammal is known for its burrowing habits and poor eyesight?", "options": ["Mole", "Rabbit", "Mouse", "Hedgehog"], "answer": "Mole"},
    {"question": "Which large feline is often black and is known for its stealth?", "options": ["Panther", "Tiger", "Lion", "Leopard"], "answer": "Panther"},
    {"question": "Which domesticated animal is often raised for its meat and is known for its snout?", "options": ["Pig", "Sheep", "Cow", "Goat"], "answer": "Pig"},
    {"question": "Which bird is known for its tuxedo-like appearance and lives in cold climates?", "options": ["Penguin", "Duck", "Seagull", "Pelican"], "answer": "Penguin"},
    {"question": "Which egg-laying mammal is known for its duck-like bill?", "options": ["Platypus", "Echidna", "Beaver", "Otter"], "answer": "Platypus"},
    {"question": "Which large bird is known for its long beak and throat pouch?", "options": ["Pelican", "Swan", "Duck", "Seagull"], "answer": "Pelican"},
    {"question": "Which large primate is known for its long arms and reddish-brown hair?", "options": ["Orangutan", "Gorilla", "Chimpanzee", "Gibbon"], "answer": "Orangutan"},
    {"question": "Which large bear is native to the Arctic and known for its white fur?", "options": ["Polar Bear", "Grizzly Bear", "Black Bear", "Panda"], "answer": "Polar Bear"},
    {"question": "Which small mammal is known for its long ears and hopping movement?", "options": ["Rabbit", "Kangaroo", "Hare", "Squirrel"], "answer": "Rabbit"},
    {"question": "Which slow-moving mammal is known for hanging upside down in trees?", "options": ["Sloth", "Monkey", "Koala", "Lemur"], "answer": "Sloth"},
    {"question": "Which bird is known for its white and gray feathers and loud calls near the sea?", "options": ["Seagull", "Pelican", "Penguin", "Duck"], "answer": "Seagull"},
    {"question": "Which small mammal is known for its reddish-brown fur and resembles a panda?", "options": ["Red Panda", "Raccoon", "Fox", "Hedgehog"], "answer": "Red Panda"},
]

challenging_questions = [
    {"question": "Name the only mammals capable of true sustained flight, excluding all other flying animals?", "options": ["Bat", "Kiwi", "Penguin", "Duck"], "answer": "Bat"},
    {"question": "Identify the insects crucial for pollination, distinguishing them from other similar creatures?", "options": ["Bee", "Ant", "Spider", "Scorpion"], "answer": "Bee"},
    {"question": "Which reptiles are large, aquatic, and have powerful jaws, but are not found in freshwater lakes?", "options": ["Crocodile", "Alligator", "Komodo Dragon", "Gharial"], "answer": "Crocodile"},
    {"question": "Determine the tallest land animals known for their extraordinary long necks?", "options": ["Giraffe", "Elephant", "Ostrich", "Camel"], "answer": "Giraffe"},
    {"question": "Which large mammals are characterized by shaggy hair and live in both North America and Eurasia?", "options": ["Bear", "Dog", "Buffalo", "Rhino"], "answer": "Bear"},
    {"question": "Identify the large carnivorous bears native to the Arctic region?", "options": ["Polar Bear", "Grizzly Bear", "Panda", "Black Bear"], "answer": "Polar Bear"},
    {"question": "Which unique mammals lay eggs and have a duck-billed appearance?", "options": ["Platypus", "Echidna", "Beaver", "Otter"], "answer": "Platypus"},
    {"question": "Which flightless birds are exclusively found in New Zealand?", "options": ["Kiwi", "Penguin", "Ostrich", "Emu"], "answer": "Kiwi"},
    {"question": "What small mammals are known for having cheek pouches and being common pets?", "options": ["Hamster", "Squirrel", "Mouse", "Chipmunk"], "answer": "Hamster"},
    {"question": "Which cunning small carnivores are famous for their reddish fur and bushy tails?", "options": ["Fox", "Wolf", "Bear", "Lion"], "answer": "Fox"},
    {"question": "Which small burrowing mammals have very poor eyesight but are proficient diggers?", "options": ["Mole", "Rabbit", "Mouse", "Hedgehog"], "answer": "Mole"},
    {"question": "Identify the marsupials renowned for their powerful hind legs and hopping locomotion?", "options": ["Kangaroo", "Koala", "Wombat", "Tasmanian Devil"], "answer": "Kangaroo"},
    {"question": "What are the fastest land animals, capable of reaching speeds up to 70 mph?", "options": ["Cheetah", "Lion", "Tiger", "Leopard"], "answer": "Cheetah"},
    {"question": "Which insects are noted for creating intricate colonies and complex social structures?", "options": ["Ant", "Bee", "Termite", "Wasp"], "answer": "Ant"},
    {"question": "Which small primates are endemic to Madagascar and known for their unique appearance?", "options": ["Lemur", "Monkey", "Orangutan", "Gibbon"], "answer": "Lemur"},
    {"question": "Which large cats are often referred to as the 'kings of the jungle'?", "options": ["Lion", "Tiger", "Panther", "Cheetah"], "answer": "Lion"},
    {"question": "What large cats are instantly recognizable by their orange coats and black stripes?", "options": ["Tiger", "Lion", "Cheetah", "Leopard"], "answer": "Tiger"},
    {"question": "Which big cats are characterized by their spotted coats and are exceptional climbers?", "options": ["Leopard", "Tiger", "Cheetah", "Lion"], "answer": "Leopard"},
    {"question": "What domesticated camelids are prized for their wool and resemble llamas?", "options": ["Alpaca", "Llama", "Camel", "Sheep"], "answer": "Alpaca"},
    {"question": "Which birds of prey are renowned for their incredible vision and hunting prowess?", "options": ["Hawk", "Eagle", "Owl", "Falcon"], "answer": "Hawk"},
    {"question": "Which adaptable seabirds are often seen near coastlines and harbors?", "options": ["Seagull", "Pelican", "Penguin", "Albatross"], "answer": "Seagull"},
    {"question": "Which crustaceans are protected by a hard exoskeleton and are commonly found in marine environments?", "options": ["Crab", "Lobster", "Shrimp", "Jellyfish"], "answer": "Crab"},
    {"question": "Which rodents are known for constructing dams and lodges?", "options": ["Beaver", "Duck", "Otter", "Rabbit"], "answer": "Beaver"},
    {"question": "Which insects play a vital role in pollination?", "options": ["Bee", "Ant", "Spider", "Scorpion"], "answer": "Bee"},
    {"question": "Which large bovines are famous for their immense strength?", "options": ["Buffalo", "Elephant", "Rhino", "Bear"], "answer": "Buffalo"},
    {"question": "Which seabirds are known for their distinctive loud calls and are often found near the sea?", "options": ["Seagull", "Pelican", "Penguin", "Duck"], "answer": "Seagull"},
    {"question": "Which small rodents are distinguished by their bushy tails?", "options": ["Squirrel", "Mouse", "Hamster", "Rat"], "answer": "Squirrel"},
    {"question": "Which small mammals are known for their spiny backs and nocturnal habits?", "options": ["Hedgehog", "Porcupine", "Rabbit", "Squirrel"], "answer": "Hedgehog"},
    {"question": "Which birds are adapted to life in the water and are unable to fly?", "options": ["Penguin", "Duck", "Ostrich", "Emu"], "answer": "Penguin"},
    {"question": "Which slow-moving mammals are known for spending most of their lives hanging upside down in trees?", "options": ["Sloth", "Koala", "Monkey", "Lemur"], "answer": "Sloth"},
    {"question": "Which domesticated ruminant mammals are typically kept as livestock for their wool and milk?", "options": ["Sheep", "Cow", "Goat", "Horse"], "answer": "Sheep"},
    {"question": "Which small mammals have long ears and are known for their rapid reproduction?", "options": ["Rabbit", "Hare", "Kangaroo", "Squirrel"], "answer": "Rabbit"},
    {"question": "Which domesticated equids are valued for their endurance and are often used as pack animals?", "options": ["Donkey", "Horse", "Camel", "Mule"], "answer": "Donkey"},
    {"question": "Which small burrowing mammals are recognized by their poor eyesight and tunneling abilities?", "options": ["Mole", "Rabbit", "Mouse", "Hedgehog"], "answer": "Mole"},
    {"question": "Which reptiles are characterized by their lack of legs?", "options": ["Snake", "Lizard", "Crocodile", "Turtle"], "answer": "Snake"},
    {"question": "Which large wild canines are famous for their social structure and pack behavior?", "options": ["Wolf", "Fox", "Coyote", "Jackal"], "answer": "Wolf"},
    {"question": "Which small mammals with reddish-brown fur are named after their resemblance to pandas?", "options": ["Red Panda", "Raccoon", "Fox", "Hedgehog"], "answer": "Red Panda"},
    {"question": "Which animals are known for their distinctive black and white striped patterns?", "options": ["Zebra", "Giraffe", "Lion", "Elephant"], "answer": "Zebra"},
]

hard_questions = [
    {"question": "Which terrestrial mammals are known for their unique proboscis, large tusks, and complex social structures, often living in matriarchal herds?", "options": ["Elephant", "Rhino", "Hippopotamus", "Giraffe"], "answer": "Elephant"},
    {"question": "Which subterranean, insectivorous mammals possess highly sensitive tactile hairs and an acute sense of touch, often leading an entirely fossorial lifestyle?", "options": ["Mole", "Rabbit", "Mouse", "Hedgehog"], "answer": "Mole"},
    {"question": "Which diurnal raptors are renowned for their acute vision, enabling them to detect small prey from kilometers away, and are often seen soaring at great heights?", "options": ["Hawk", "Eagle", "Owl", "Falcon"], "answer": "Hawk"},
    {"question": "Which arboreal marsupials, native to Australia, exhibit a sedentary lifestyle primarily consuming toxic eucalyptus leaves and possessing a specialized cecum for detoxification?", "options": ["Koala", "Kangaroo", "Wombat", "Tasmanian Devil"], "answer": "Koala"},
    {"question": "Which carnivorous marsupials, endemic to Tasmania, are characterized by their robust jaws, nocturnal habits, and a unique form of vocalization that resembles a high-pitched scream?", "options": ["Tasmanian Devil", "Kangaroo", "Koala", "Wombat"], "answer": "Tasmanian Devil"},
    {"question": "Which eusocial insects, essential for cross-pollination in various ecosystems, are known for their complex communication through dance and pheromones?", "options": ["Bee", "Ant", "Spider", "Scorpion"], "answer": "Bee"},
    {"question": "Which omnivorous mammals are distinguished by their bulky frame, plantigrade locomotion, and varied diet that includes berries, fish, and occasionally small mammals?", "options": ["Bear", "Dog", "Buffalo", "Rhino"], "answer": "Bear"},
    {"question": "Which bovid species are notable for their substantial size, curved horns, and significant role in both agricultural societies and natural grassland ecosystems?", "options": ["Buffalo", "Elephant", "Rhino", "Bear"], "answer": "Buffalo"},
    {"question": "Which large felids, recognized for their distinctive black tear streaks, can accelerate from 0 to 60 miles per hour in just a few seconds, making them the fastest land animals?", "options": ["Cheetah", "Lion", "Tiger", "Leopard"], "answer": "Cheetah"},
    {"question": "Which nocturnal, flightless birds, native to New Zealand, possess a highly developed olfactory system and are the only birds with nostrils at the end of their beak?", "options": ["Kiwi", "Penguin", "Ostrich", "Emu"], "answer": "Kiwi"},
    {"question": "Which small fossorial mammals exhibit a cylindrical body, reduced eyes, and specialized digging forelimbs, allowing them to create extensive underground tunnel networks?", "options": ["Mole", "Rabbit", "Mouse", "Hedgehog"], "answer": "Mole"},
    {"question": "Which opportunistic seabirds are highly adaptable, often exhibiting kleptoparasitic behavior, and are frequently observed in coastal and urban environments scavenging for food?", "options": ["Seagull", "Pelican", "Penguin", "Albatross"], "answer": "Seagull"},
    {"question": "Which small rodents are characterized by their expandable cheek pouches, which they use to transport food back to their burrows for storage?", "options": ["Hamster", "Squirrel", "Mouse", "Chipmunk"], "answer": "Hamster"},
    {"question": "Which vulpine species, known for their cunning nature, exhibit complex problem-solving abilities and are featured in numerous cultural mythologies and fables?", "options": ["Fox", "Wolf", "Bear", "Lion"], "answer": "Fox"},
    {"question": "Which flightless seabirds, residing primarily in the Southern Hemisphere, are adapted to cold environments with their dense, waterproof feathers and a layer of insulating fat?", "options": ["Penguin", "Duck", "Seagull", "Pelican"], "answer": "Penguin"},
    {"question": "Which small insectivorous mammals are covered in spines, which they erect as a defense mechanism when threatened, and often roll into a tight ball for protection?", "options": ["Hedgehog", "Porcupine", "Rabbit", "Squirrel"], "answer": "Hedgehog"},
    {"question": "Which semi-aquatic rodents, known for their engineering skills, construct dams and lodges that create wetland habitats, benefiting various other species?", "options": ["Beaver", "Duck", "Otter", "Rabbit"], "answer": "Beaver"},
    {"question": "Which large, herbivorous mammals possess one or two keratinous horns on their snouts and are critically endangered due to poaching and habitat loss?", "options": ["Rhino", "Elephant", "Lion", "Giraffe"], "answer": "Rhino"},
    {"question": "Which arachnids are distinguished by their ability to spin silk webs, used for capturing prey, creating shelters, and as a means of communication?", "options": ["Spider", "Scorpion", "Tick", "Mite"], "answer": "Spider"},
    {"question": "Which domesticated camelids, closely related to llamas, are prized for their soft and luxurious wool, which is used in the textile industry?", "options": ["Alpaca", "Llama", "Camel", "Sheep"], "answer": "Alpaca"},
    {"question": "Which large cats are recognized by their rosette-patterned coats, solitary behavior, and exceptional climbing abilities, often storing their kills in trees?", "options": ["Leopard", "Tiger", "Cheetah", "Lion"], "answer": "Leopard"},
    {"question": "Which social felids, often referred to as the kings of the jungle, live in prides and exhibit a distinctive mane in males?", "options": ["Lion", "Tiger", "Panther", "Cheetah"], "answer": "Lion"},
    {"question": "Which apex predators, known for their orange coats and vertical black stripes, primarily inhabit forests and grasslands in Asia?", "options": ["Tiger", "Lion", "Cheetah", "Leopard"], "answer": "Tiger"},
    {"question": "Which ungulates are notable for their long necks, allowing them to browse foliage high in trees, and are the tallest living terrestrial animals?", "options": ["Giraffe", "Elephant", "Ostrich", "Camel"], "answer": "Giraffe"},
    {"question": "Which marsupials, recognized for their powerful hind legs and tail, engage in bipedal locomotion through hopping, and are iconic to Australia?", "options": ["Kangaroo", "Koala", "Wombat", "Tasmanian Devil"], "answer": "Kangaroo"},
    {"question": "Which small, nearly blind, subterranean mammals create extensive tunnel systems and have velvety fur adapted for their underground lifestyle?", "options": ["Mole", "Rabbit", "Mouse", "Hedgehog"], "answer": "Mole"},
    {"question": "Which large reptiles, with elongated bodies and powerful tails, are found in tropical regions and are known for their predatory behavior and strong jaws?", "options": ["Crocodile", "Alligator", "Komodo Dragon", "Gharial"], "answer": "Crocodile"},
    {"question": "Which herbivorous mammals, native to Africa, are recognizable by their black and white striped coats and often form harems or small herds?", "options": ["Zebra", "Giraffe", "Lion", "Elephant"], "answer": "Zebra"},
    {"question": "Which small mammals are noted for their spiny backs and nocturnal foraging habits, often feeding on insects and small invertebrates?", "options": ["Hedgehog", "Porcupine", "Rabbit", "Squirrel"], "answer": "Hedgehog"},
    {"question": "Which arboreal mammals, native to the Eastern Himalayas and Southwestern China, are closely related to raccoons and exhibit a reddish-brown fur and a ringed tail?", "options": ["Red Panda", "Raccoon", "Fox", "Hedgehog"], "answer": "Red Panda"},
    {"question": "Which lagomorphs are known for their long ears, powerful hind legs, and ability to reproduce rapidly, often considered pests in agricultural areas?", "options": ["Rabbit", "Hare", "Kangaroo", "Squirrel"], "answer": "Rabbit"},
    {"question": "Which small rodents are known for their bushy tails, ability to climb trees, and habit of burying nuts for winter storage?", "options": ["Squirrel", "Mouse", "Hamster", "Rat"], "answer": "Squirrel"},
    {"question": "Which small, fossorial mammals are characterized by their poor eyesight and specialized forelimbs for digging intricate tunnel systems?", "options": ["Mole", "Rabbit", "Mouse", "Hedgehog"], "answer": "Mole"},
    {"question": "Which large seabirds have an expansive throat pouch used for catching fish and are often seen gliding gracefully over water surfaces?", "options": ["Pelican", "Swan", "Duck", "Seagull"], "answer": "Pelican"},
    {"question": "Which arboreal mammals, known for their slow movement and distinctive three-toed limbs, spend most of their lives hanging upside down in trees?", "options": ["Sloth", "Monkey", "Koala", "Lemur"], "answer": "Sloth"},
    {"question": "Which large primates, distinguished by their reddish fur and solitary nature, primarily inhabit the rainforests of Borneo and Sumatra?", "options": ["Orangutan", "Gorilla", "Chimpanzee", "Gibbon"], "answer": "Orangutan"},
    {"question": "Which carnivorous marsupials, endemic to Tasmania, are recognized for their powerful jaws, scavenging behavior, and distinct vocalizations?", "options": ["Tasmanian Devil", "Kangaroo", "Koala", "Wombat"], "answer": "Tasmanian Devil"},
]

# Function to wrap text to a specified width
def wrap_text(text, width):
    return "\n".join(textwrap.fill(line, width) for line in text.split("\n"))

# Function to randomize the order of options in a question
def randomize_options(question):
    options = question['options']
    random.shuffle(options)
    return options

# Function to load multiple-choice question into the quiz window
def load_mc_question(quiz_window, idx, score, questions):
    # Clear the previous widgets from the quiz window
    for widget in quiz_window.winfo_children():
        widget.destroy()

    # Get the current question and display it
    question = questions[idx]
    question_label = tk.Label(quiz_window, text=f"Question {idx + 1}: {question['question']}", font=("Helvetica", 14, "bold"), bg="white", wraplength=550, justify=tk.LEFT)
    question_label.pack(pady=10)

    # Entry widget for the answer
    answer_entry = tk.Entry(quiz_window, font=("Helvetica", 14), width=40)
    answer_entry.pack(pady=5)

    # Frame to hold the options
    options_frame = tk.Frame(quiz_window, bg="white")
    options_frame.pack(pady=10)

    # Randomize and display the options
    options = randomize_options(question)
    for i, option in enumerate(options):
        option_label = tk.Label(options_frame, text=f"{chr(65 + i)}. {option}", font=("Helvetica", 14), width=20, height=2, bg="lightgray", relief="groove")
        option_label.grid(row=i//2, column=i%2, padx=5, pady=5)

    # Label to provide feedback to the user
    feedback_label = tk.Label(quiz_window, text="", font=("Helvetica", 12), bg="white")
    feedback_label.pack(pady=5)

    # Submit button to check the answer and proceed to the next question
    submit_button = tk.Button(quiz_window, text="Submit", font=("Helvetica", 14),
                              command=lambda: display_next_mc_question(quiz_window, idx, score, questions, answer_entry, feedback_label, submit_button))
    submit_button.pack(pady=10)

# Function to handle the display of the next multiple-choice question
def display_next_mc_question(quiz_window, idx, score, questions, answer_entry, feedback_label, submit_button):
    answer = answer_entry.get().strip().capitalize()
    correct_option = questions[idx]['answer']
    option_letters = ['A', 'B', 'C', 'D']
    options = questions[idx]['options']
    valid_options = option_letters + [opt.capitalize() for opt in options]

    # Check if the answer is valid and correct
    if answer in valid_options:
        if answer == correct_option or (answer in option_letters and options[option_letters.index(answer)] == correct_option):
            feedback_label.config(text="Correct!", fg="green")
            score += 1
        else:
            feedback_label.config(text=f"Incorrect! The correct answer was {correct_option}", fg="red")

        # Update the submit button to load the next question or show results if it was the last question
        submit_button.config(text="Next Question",
                             command=lambda: load_mc_question(quiz_window, idx + 1, score, questions) if idx < len(questions) - 1 else show_results(quiz_window, score, questions))
    else:
        feedback_label.config(text="Please enter a valid option (A, B, C, D) or animal name.", fg="red")

# Function to display the quiz results
def show_results(quiz_window, score, questions):
    # Clear the previous widgets from the quiz window
    for widget in quiz_window.winfo_children():
        widget.destroy()

    # Display the user's score
    result_label = tk.Label(quiz_window, text=f"Your Score: {score}/{len(questions)}", font=("Helvetica", 18, "bold"), bg="white")
    result_label.pack(pady=20)

    # Button to close the quiz window
    close_button = tk.Button(quiz_window, text="Close", command=quiz_window.destroy, font=("Helvetica", 14))
    close_button.pack(pady=10)

# Function to start the quiz based on the selected difficulty level
def start_quiz(difficulty, questions):
    close_previous_window()

    quiz_window = tk.Toplevel()
    quiz_window.title(f"Who Can Do That? Quiz - {difficulty.capitalize()} Mode")
    quiz_window.geometry("600x400")
    quiz_window.configure(bg="white")

    quiz_window.protocol("WM_DELETE_WINDOW", lambda: close_window(quiz_window))

    window_stack.append(quiz_window)

    load_mc_question(quiz_window, 0, 0, questions)

# Function to close the current window and show the previous one if any
def close_window(window_to_close=None):
    global window_stack
    if window_stack:
        current_window = window_stack.pop()
        current_window.destroy()
    if window_stack:
        last_window = window_stack[-1]
        last_window.deiconify()
    else:
        open_difficulty_selection()  # Reopen the difficulty selection menu if no other windows are open

# Function to hide the current window without destroying it
def close_previous_window():
    if window_stack:
        window_stack[-1].withdraw()

# Function to open the difficulty selection window
# Function to open the difficulty selection window
def open_difficulty_selection():
    global difficulty_window
    difficulty_window = tk.Toplevel()
    difficulty_window.title("Select Difficulty:")
    difficulty_window.geometry("400x400")
    difficulty_window.configure(bg="white")

    # Display the title and difficulty options
    title_label = tk.Label(difficulty_window, text="Select Difficulty", font=("Helvetica", 24, "bold"), bg="white")
    title_label.pack(pady=20)

    easy_button = tk.Button(difficulty_window, text="Easy", width=25, height=2, bg="green", font=("Helvetica", 16, "bold"), command=lambda: start_quiz("easy", easy_questions))
    easy_button.pack(pady=15)

    challenging_button = tk.Button(difficulty_window, text="Challenging", width=25, height=2, bg="yellow", font=("Helvetica", 16, "bold"), command=lambda: start_quiz("challenging", challenging_questions))
    challenging_button.pack(pady=15)

    hard_button = tk.Button(difficulty_window, text="Hard", width=25, height=2, bg="red", font=("Helvetica", 16, "bold"), command=lambda: start_quiz("hard", hard_questions))
    hard_button.pack(pady=15)

    difficulty_window.protocol("WM_DELETE_WINDOW", root.destroy)
    window_stack.append(difficulty_window)

# Create the root window and immediately open the difficulty selection window
root = tk.Tk()
root.withdraw()  # Hide the root window

open_difficulty_selection()

root.mainloop()
