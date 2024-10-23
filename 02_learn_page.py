import tkinter as tk
from PIL import Image, ImageTk

# Global variables to store the animal list and descriptions
animal_list = sorted(["Alpaca", "Ant", "Bat", "Bee", "Crocodile", "Deer", "Cheetah", "Duck",
                      "Crab", "Spider", "Rhino", "Cat", "Dog", "Giraffe", "Bear", "Elephant", "Tiger",
                      "Lion", "Zebra", "Kangaroo", "Buffalo", "Beaver", "Donkey", "Tasmanian Devil", "Hamster", "Hawk",
                      "Fox", "Hedgehog", "Horse", "Kiwi", "Lizard", "Leopard", "Koala", "Lemur", "Mole", "Panther",
                      "Pig", "Penguin", "Platypus", "Pelican", "Orangutan", "Polar Bear", "Rabbit", "Sloth", "Seagull",
                      "Red Panda", "Snake", "Sheep", "Squirrel", "Turkey", "Wolf", "Wombat"])

# Dictionary to store descriptions of animals
animal_descriptions = {
    "bear": "Bears exhibit a range of physical appearances and colors depending on their species and habitats. "
            "From the majestic white coat of polar bears to the sleek black fur of black bears, and the brown hues"
            " of grizzly bears, their diverse colorations blend with their environments for camouflage and insulation."
            " Bears are characterized by their robust builds, powerful limbs with sharp claws, and distinctive facial "
            "features like large heads with strong jaws and keen eyesight. These physical attributes make them "
            "formidable predators and efficient foragers across a variety of landscapes."
            "\n\n In terms of abilities and "
            "strengths, bears are renowned for their immense physical power. They can lift heavy objects, climb trees "
            " with ease using their sharp claws, and swim long distances proficiently. Bears possess keen senses of"
            " smell and hearing, aiding in their hunting and scavenging efforts. Their omnivorous diet allows them to "
            "adapt to different food sources, while some species hibernate during winter months to conserve energy. "
            "Bears' maternal instincts are also notable, with females fiercely protecting their cubs against potential"
            " threats. These combined abilities make bears versatile and successful in their respective ecosystems",

    "cat": "Cats come in various shapes, sizes, and colors, each adapted to their environment and lifestyle. From the"
           " sleek, slender bodies of domestic cats to the muscular builds of wildcats like tigers and lions, their "
           "physical appearance varies widely. Their fur can range from solid colors like black, white, or gray to"
           " intricate patterns such as tabby stripes, spots, or rosettes. Cats have sharp retractable claws that"
           " they use for hunting, climbing, and defense, along with keen senses including excellent night vision,"
           " acute hearing, and a strong sense of smell. Their flexible bodies, agile movements, and whiskers aid "
           "in navigating their surroundings with precision. \n\n"
           "In terms of abilities and strengths, cats are known "
           "for their agility, stealth, and hunting prowess. They are exceptional climbers, capable of scaling trees"
           " and vertical surfaces effortlessly. Cats have quick reflexes and are skilled hunters, using their sharp"
           " claws and teeth to catch prey. Their retractable claws allow for silent stalking, making them efficient"
           " predators. Cats also have remarkable balance and coordination, enabling them to leap and pounce with "
           "accuracy. Additionally, domestic cats exhibit strong social bonds with humans, displaying affection through"
           " purring, grooming, and playful behaviors. Overall, cats' physical abilities and adaptability contribute to"
           " their success as both predators and companions in various environments.",

    "dog": "Dogs display a wide range of physical appearances, sizes, and coat colors, reflecting the diversity of "
           "their breeds and roles. From the compact, fluffy bodies of toy breeds like Pomeranians to the muscular"
           " frames of working breeds such as German Shepherds and Rottweilers, dogs come in various shapes. Their "
           "fur can be short, long, curly, or wiry, with colors spanning from solid shades like black, white, brown,"
           " and tan to multicolor patterns and markings. Dogs have strong, adaptable jaws with sharp teeth suited "
           "for chewing, tearing, and grasping objects. Their keen senses include acute hearing, a strong sense of "
           "smell, and decent vision, making them adept hunters and loyal companions. \n\n"
           "In terms of abilities and "
           "strengths, dogs are known for their loyalty, intelligence, and versatility. They have strong bonds with"
           " humans, often displaying protective and affectionate behaviors towards their owners. Dogs excel in a wide"
           " range of tasks, from herding and guarding to search and rescue, owing to their trainable nature and "
           "willingness to work. They are skilled at tracking scents, making them valuable in law enforcement and "
           "detection roles. Dogs also possess great endurance and stamina, enabling them to engage in various"
           " physical activities like running, fetching, and agility training. Additionally, their social nature "
           "allows them to thrive in pack environments and form strong relationships with other animals and humans"
           " alike. Overall, dogs' physical abilities, combined with their loyalty and adaptability, make them "
           "cherished companions and valuable working partners across different domains.",

    "sheep": "Sheep are known for their distinct physical characteristics and behaviors that suit their grazing "
             "lifestyle. They typically have compact bodies covered in woolly fleece that can vary in color from "
             "white, black, brown, or a mix of these shades. Their woolly coats provide insulation against cold"
             " weather and protection from environmental elements. Sheep have relatively short legs and hooves "
             "specialized for navigating uneven terrain, such as grassy pastures and rocky hillsides. Their heads"
             " are adorned with curved horns in some breeds, while others have hornless varieties. Sheep have a "
             "herbivorous diet, primarily feeding on grasses, plants, and occasional supplements. \n\n"
             "In terms of "
             "abilities and strengths, sheep are well-adapted to grazing and flock living. They have excellent "
             "peripheral vision and a heightened sense of hearing, allowing them to detect potential threats from "
             "predators. Sheep are social animals that prefer to graze and move together in groups, offering safety"
             " in numbers. They also exhibit strong flocking instincts, following a hierarchy within the group and"
             " relying on collective behaviors for protection. Sheep are known for their wool production, with"
             " breeds like Merinos prized for their fine, soft wool used in textiles. Additionally, sheep have "
             "been domesticated for centuries, showcasing their docile nature and suitability for agricultural "
             "purposes such as meat and wool production. Overall, sheep's physical attributes and social behaviors"
             " make them valuable livestock animals in farming and ranching operations worldwide.",

    "alpaca": "Alpacas are unique camelid species known for their distinct physical features and valuable fleece. "
              "They have slender bodies with long necks and legs, covered in soft, dense fleece that comes in a "
              "variety of natural colors including white, brown, black, and shades of gray. Alpacas are similar in "
              "appearance to llamas but are smaller in size. They have large, expressive eyes and long ears that "
              "give them an alert and curious look. Alpacas are domesticated animals primarily bred for their luxurious"
              " fleece, which is prized for its warmth, softness, and hypoallergenic properties. \n\n"
              " In terms of "
              " and strengths, alpacas are well-adapted to their native mountainous environments in South America. "
              "They have padded feet with soft pads that allow them to navigate rocky terrain with ease. Alpacas are "
              "herbivores, feeding on grasses and plants, and they have a specialized three-chambered stomach for"
              " efficient digestion. They are social animals that prefer to live in herds, exhibiting strong bonds "
              "with their herd members. Alpacas are gentle and docile, making them popular as pets and companions "
              "in addition to their role in fiber production. They are also known for their alertness and protective"
              " instincts, often sounding alarm calls to alert the herd of potential threats from predators. Overall,"
              " alpacas are prized for their fleece quality, gentle temperament, and adaptability to various climates,"
              " making them valuable animals in agriculture and as pets.",

    "ant": "Ants are fascinating insects known for their highly organized social structures and impressive abilities."
           " Physically, ants typically have segmented bodies with three main parts: the head, thorax, and abdomen. "
           "They are typically small in size, ranging from a few millimeters to a few centimeters in length, depending"
           " on the species. Ants come in various colors, including black, brown, red, and yellow, with some species "
           "exhibiting patterns or markings on their bodies. They have six legs and antennae that they use for sensing "
           "their environment, communicating with each other, and detecting food sources. \n\n" 
           "In terms of abilities and "
           "strengths, ants are incredibly strong for their size, capable of carrying objects many times heavier than "
           "themselves. They achieve this feat through coordinated teamwork, with multiple ants working together to "
           "transport larger items back to their colony. Ants are also known for their impressive digging abilities,"
           " creating intricate underground tunnels and chambers for their nests. They are efficient scavengers and "
           "foragers, using pheromone trails to communicate and navigate between food sources and their colony. Ants "
           "are highly organized, with specialized roles within their colonies such as workers, soldiers, and the queen"
           " responsible for reproduction. Some species of ants exhibit complex farming behaviors, cultivating fungus "
           "within their nests as a food source. Overall, ants' collective intelligence, strength, and adaptability"
           " make them successful and resilient insects in various ecosystems around the world.",

    "bat": "Bats are unique mammals renowned for their ability to fly, facilitated by their elongated finger bones "
           "supporting a leathery wing membrane. They come in various sizes and colors, blending into their "
           "environments with fur shades ranging from brown to black or gray. What sets bats apart is their"
           " remarkable echolocation skills, emitting high-frequency sounds to navigate in the dark, locate prey "
           "like insects or fruits, and avoid obstacles while in flight. This biological sonar aids their nocturnal "
           "lifestyle, allowing them to thrive as efficient insectivores, pollinators, and seed dispersers in diverse"
           " ecosystems. \n\n"
           "Socially, bats exhibit fascinating behaviors within their colonies, communicating through"
           " vocalizations and engaging in grooming rituals. They form strong maternal bonds, with females nurturing "
           "and caring for their young pups. Bats play vital roles in maintaining ecological balance, controlling "
           "insect populations, and contributing to plant pollination and seed dispersal, highlighting their"
           " significance in global biodiversity and ecosystem health.",

    "bee": "Bees are fascinating insects known for their complex social structures, vital role in pollination, and "
           "unique physical adaptations. They typically have a compact body with three main parts: the head, thorax, "
           "and abdomen. Bees are covered in fine hairs that help collect pollen, which they use as food for themselves"
           " and their young. Their wings are transparent and delicate, allowing for efficient flight. Bees are"
           " well-known for their ability to produce honey, which they create by collecting nectar from flowers and"
           " processing it in their hives. \n\n"
           "In terms of abilities and strengths, bees are exceptional pollinators,"
           " playing a crucial role in the reproduction of many plant species, including fruits, vegetables, and "
           "flowers. They have specialized pollen baskets on their hind legs for carrying pollen back to the hive. Bees"
           " also have a highly developed sense of smell and use intricate dances, known as the waggle dance, to "
           "communicate the location of food sources to other members of the hive. Within their colonies, bees exhibit"
           " organized social behaviors, with distinct roles for worker bees, drones, and the queen bee. Their "
           "collective efforts in pollination, honey production, and hive maintenance make bees essential contributors "
           "to ecosystems and agricultural sustainability.",

    "crocodile": "Crocodiles are large, aquatic reptiles with a distinctive physical appearance and formidable "
                 "abilities. They have elongated bodies covered in armored scales, providing protection against "
                 "predators and environmental hazards. Crocodiles have powerful jaws lined with sharp teeth, capable"
                 " of delivering crushing bites to prey. Their eyes and nostrils are positioned on top of their heads,"
                 "allowing them to remain submerged while keeping an eye out for potential prey or threats. Crocodiles"
                 " come in various species, ranging in size from the smaller freshwater crocodiles to the massive "
                 "saltwater crocodiles, which are among the largest reptiles on Earth. \n\n"
                 "In terms of abilities and "
                 "strengths, crocodiles are highly adapted predators both in water and on land. They are excellent "
                 "swimmers, using their strong tails to propel themselves through the water with remarkable speed and"
                 " agility. Crocodiles are ambush predators, patiently waiting for prey to approach before launching "
                 "into swift and powerful attacks. Their ability to regulate their body temperature allows them to "
                 "thrive in diverse habitats, from freshwater rivers and lakes to coastal estuaries and swamps. "
                 "Crocodiles are also known for their longevity, with some species living for several decades or more. "
                 "Overall, crocodiles play important roles in their ecosystems as top predators, helping to regulate "
                 "prey populations and maintain ecological balance.",

    "deer": "Deer are graceful, herbivorous mammals known for their slender bodies, long legs, and branching antlers"
            " (in males of most species). They have a compact head with large eyes positioned on the sides, giving them"
            " a wide field of vision to detect potential threats. Deer come in various species, such as white-tailed"
            " deer, mule deer, elk, and moose, each with its unique physical characteristics and habitat preferences."
            " Their fur can range in color from reddish-brown to gray or even white, adapting to seasonal changes and"
            " providing camouflage in their environments. \n\n"
            "In terms of abilities and strengths, deer are renowned for"
            " their agility, speed, and keen senses. They are excellent runners, capable of reaching high speeds to "
            "evade predators or navigate challenging terrain. Deer have acute senses of hearing and smell, allowing "
            "them to detect danger and forage for food effectively. Their herbivorous diet consists mainly of grasses,"
            " leaves, twigs, and fruits, contributing to the dispersion of seeds and the maintenance of plant "
            "diversity. Male deer, known as bucks, grow antlers annually, which they use for display during mating "
            "season and sometimes for defense against rivals. Overall, deer are vital components of ecosystems, "
            "contributing to nutrient cycling, plant dispersal, and serving as prey for carnivores in natural"
            " food chains.",

    "cheetah": "The cheetah is a fascinating big cat known for its incredible speed and sleek physical appearance. It "
               "has a slender, aerodynamic body with a deep chest and long legs designed for explosive acceleration. "
               "Cheetahs are covered in a yellowish-tan coat with distinctive black spots, aiding in camouflage within"
               " their grassland habitats. They have a small, rounded head with distinctive black tear stripes running "
               "from the eyes to the nose, which help reduce glare from the sun during hunts. Cheetahs are also known "
               "for their long, muscular tail, which aids in balance and steering during high-speed chases. \n\n"
               " In terms of"
               " abilities and strengths, cheetahs are unmatched in their speed and agility among land animals. They"
               " can sprint at speeds of up to 60-70 miles per hour (96-113 kilometers per hour) in short bursts,"
               " making them the fastest land mammals. Their flexible spine, semi-retractable claws, and specialized "
               "leg muscles contribute to their swift running capabilities. Cheetahs rely on their keen eyesight to"
               " spot prey from a distance and execute precise, high-speed pursuits to catch smaller ungulates like"
               " gazelles and impalas. They are solitary hunters, using stealth and camouflage to get as close as "
               "possible before launching their rapid attacks. Despite their impressive speed, cheetahs are also "
               "vulnerable to larger predators like lions and hyenas, often losing their kills to these competitors. "
               "Overall, the cheetah's unique physical adaptations and unparalleled speed make it a remarkable predator"
               " in the African savannah ecosystem.",

    "duck": "Ducks are aquatic birds known for their distinctive physical features and behaviors. They have compact "
            "bodies with short necks and webbed feet, ideal for swimming and diving in water. Ducks come in various "
            "species, each with its unique coloration and markings, from the vibrant mallard ducks with their green "
            "heads and iridescent feathers to the striking mandarin ducks with their colorful plumage. They have "
            "waterproof feathers that keep them dry and buoyant while swimming, thanks to the oil produced by a gland "
            "near their tails. \n\n"
            "In terms of abilities and strengths, ducks are well-adapted to life in and around water."
            " They are excellent swimmers, using their webbed feet for paddling and their wings for balance. Ducks have"
            " a broad diet that includes aquatic plants, insects, small fish, and crustaceans, making them "
            "opportunistic feeders. They also play important roles in ecosystems as seed dispersers, contributing "
            "to the spread of plants and maintaining wetland habitats. Ducks are social birds, often seen in groups "
            "or flocks, especially during migration seasons. They have distinct vocalizations and behaviors for"
            " communication within their groups and to warn of potential threats. Overall, ducks' adaptability, "
            "swimming abilities, and social behaviors make them fascinating and integral parts of wetland ecosystems"
            " worldwide.",

    "crab": "Crabs are fascinating crustaceans with a distinctive appearance and unique adaptations for life in aquatic"
            " environments. They have a hard, shell-like exoskeleton that protects their bodies, typically featuring a"
            " broad, flattened shape with ten legs, including a pair of pincers (chelae) at the front. Crabs come in "
            "various sizes, colors, and species, ranging from small hermit crabs that inhabit shells to larger species"
            " like king crabs and blue crabs. Their exoskeletons undergo molting as they grow, shedding old shells to "
            "reveal new ones underneath. \n\n"
            "In terms of abilities and strengths, crabs are well-equipped for survival in"
            " diverse marine habitats. They are skilled scavengers and omnivores, feeding on a range of foods such as "
            "algae, small fish, mollusks, and detritus. Crabs' chelae are used for capturing and manipulating prey,"
            " defending against predators, and communication with other crabs. They have powerful muscles for "
            "locomotion, enabling them to crawl, swim, and burrow into substrates like sand or mud. Many crab species"
            " are excellent burrowers, creating intricate tunnels and burrows for shelter and protection. Crabs also "
            "play vital roles in marine ecosystems, contributing to nutrient cycling, scavenging dead organisms, and "
            "serving as prey for larger predators. Overall, crabs' unique anatomy, feeding behaviors, and habitat "
            "adaptations make them fascinating and important components of marine biodiversity.",

    "spider": "Spiders are intriguing arachnids known for their eight legs, multiple eyes, and silk-producing "
              "abilities. Their bodies are divided into two segments: the cephalothorax, which combines the head and "
              "thorax, and the abdomen. Spiders utilize specialized structures called spinnerets, located at the rear "
              "of their abdomen, to produce silk threads used for various purposes such as building webs, constructing"
              " egg sacs, and creating draglines for movement. They come in a wide range of sizes and colors, from "
              "small and agile jumping spiders to larger and slower tarantulas, each adapted to different hunting "
              "techniques and habitats. \n\n"
              "In terms of abilities and strengths, spiders are skilled predators that play"
              " vital roles in controlling insect populations within ecosystems. They employ diverse hunting "
              "strategies, including ambush hunting, web hunting, and active hunting, using venom injected through"
              " their fangs to immobilize prey. Spiders' multiple eyes, typically arranged in clusters, provide them"
              " with keen vision for detecting movement and potential threats. Despite their sometimes intimidating "
              "appearance, most spider species are harmless to humans and prefer to avoid confrontation. Their "
              "fascinating silk production, predatory behaviors, and ecological importance make spiders intriguing "
              "subjects for scientific study and essential components of biodiversity.",

    "rhino": "Rhinos, which is a large herbivorous mammal with a distinctive horn or horns on its snout. Rhinos are"
             " known for their powerful build, thick skin, and massive size. They typically have a thick-set "
             "body, short legs, and a large head with a horn made of keratin, the same material as human hair"
             " and nails. There are five species of rhinoceros: the white rhinoceros, black rhinoceros, Indian"
             " rhinoceros, Javan rhinoceros, and Sumatran rhinoceros, each with its unique characteristics"
             " and habitat preferences. \n\n"
             "In terms of abilities and strengths, rhinos are known for their "
             "formidable presence and defensive capabilities. Despite their large size and weight, rhinos"
             " are surprisingly agile and can reach speeds of up to 30 miles per hour (48 kilometers per "
             "hour) when charging. Their thick, tough skin provides protection against predators and "
             "environmental hazards. Rhinos have acute senses of hearing and smell, aiding in detecting "
             "threats and locating food sources. They are herbivores, feeding mainly on grasses, leaves, "
             "fruits, and shrubs, using their prehensile lips to grasp and consume vegetation. Rhinos also "
             "play crucial roles in their ecosystems as grazers, seed dispersers, and contributors to nutrient"
             " cycling. Overall, rhinos' physical attributes, defensive capabilities, and ecological"
             " significance make them iconic and important members of the animal kingdom.",

    "giraffe": "Giraffes are iconic mammals recognized for their towering height, long necks, and distinctive "
               "spotted patterns. They have slender bodies supported by long legs, enabling them to browse tall "
               "trees for leaves, their primary food source. Giraffes' necks can be over six feet long, containing "
               "the same number of vertebrae as humans but elongated. Their fur coat varies in color, ranging from "
               "light tan to dark brown, adorned with irregular patches or spots that help camouflage them in "
               "savannah habitats. Giraffes have large, expressive eyes and long eyelashes, enhancing their vision "
               "and protecting against dust and debris. Their tongues are prehensile and can extend up to 18 inches,"
               " allowing them to grasp and pull leaves from high branches. \n\n" 
               "In terms of abilities and strengths, "
               "giraffes are adapted to their browsing lifestyle, with specialized cardiovascular systems that "
               "regulate blood flow to their heads when lowering or raising them. They are agile despite their size,"
               " capable of running at speeds up to 35 miles per hour and using their long legs to deliver powerful "
               "kicks as a defense mechanism. Giraffes are social animals that form loose herds, exhibiting "
               "hierarchical structures and engaging in social behaviors such as grooming and necking (sparring "
               "with their necks). Their unique appearance, gentle demeanor, and role as browsers make them "
               "integral to African ecosystems.",

    "elephant": "Elephants are majestic mammals known for their large size, distinctive trunk, tusks, and social "
                "structures. They have robust bodies supported by thick legs and padded feet, capable of carrying "
                "their massive weight. Elephants' trunks are elongated muscular structures with numerous functions, "
                "including breathing, smelling, grasping objects, and producing sounds. They are herbivores, feeding "
                "primarily on grasses, leaves, fruits, and bark. Elephants have complex social behaviors, living in "
                "herds led by matriarchs, with strong familial bonds among members. They communicate through vocalizations,"
                " body language, and tactile interactions, displaying empathy, cooperation, and protective instincts "
                "within their groups. \n\n" 
                "In terms of abilities and strengths, elephants are incredibly intelligent and "
                "adaptive, capable of problem-solving, memory retention, and emotional connections. They have keen "
                "senses, including acute hearing and an excellent sense of smell, helping them navigate environments, "
                "detect threats, and communicate over long distances. Elephants are also skilled swimmers, using "
                "water bodies for bathing, cooling off, and accessing new food sources. Despite their formidable size, "
                "elephants are known for their gentle demeanor and nurturing behaviors, particularly towards calves "
                "and herd members in need. Their role as keystone species in ecosystems contributes to seed dispersal, "
                "habitat shaping, and ecological balance in savannahs, forests, and wetlands.",

    "tiger": "Tigers are powerful and majestic big cats known for their striped fur patterns, stealthy hunting "
             "abilities, and status as apex predators. They have muscular bodies, round heads with strong jaws,"
             " and distinctive black stripes on their orange or yellow fur coats, providing effective camouflage in"
             " forested and grassland habitats. Tigers' fur patterns are unique to each individual, similar to human"
             " fingerprints. They have keen senses, including sharp vision, acute hearing, and a strong sense of"
             " smell, making them efficient hunters both day and night. Tigers are solitary animals, establishing"
             " large territories that they mark with scent markings and vocalizations. They are adept swimmers,"
             " using water bodies for cooling off, traveling, and hunting prey such as deer, wild boar, and"
             " antelopes. Tigers are territorial and often confrontational with other tigers, particularly males"
             " defending their territories or seeking mates. \n\n"
             "In terms of abilities and strengths, tigers are among"
             " the strongest and most agile big cats, capable of leaping great distances, climbing trees, and"
             " delivering powerful strikes with their paws. They are skilled stalkers and ambush predators, using"
             " cover and stealth to approach prey before launching a swift and deadly attack. Tigers play crucial"
             " roles in ecosystems as top predators, regulating prey populations and maintaining biodiversity. However,"
             " tiger populations are endangered due to habitat loss, poaching for their skins and body parts, human-"
             " wildlife conflicts, and illegal wildlife trade. Conservation efforts and protection of tiger habitats"
             " are essential for their survival and the preservation of balanced ecosystems.",

    "lion": "Lions are majestic big cats renowned for their strength, social structures, and hunting prowess. They "
            "have muscular bodies, round heads with powerful jaws, and golden fur coats, with males sporting "
            "distinctive manes around their necks. Lionesses are typically smaller and lack manes, focusing on "
            "hunting and raising cubs within the pride. Lions are social animals that form prides consisting of "
            "related females and their offspring, along with a coalition of dominant males. They exhibit "
            "territorial behaviors, marking their territories with scent markings and vocalizations. \n\n"
            "Lions are "
            "apex predators, preying on a variety of animals including antelopes, zebras, and wildebeests. They "
            "are known for their cooperative hunting strategies, with lionesses working together to stalk, chase,"
            " and bring down prey for the pride. Lions have exceptional night vision and keen senses, making them"
            " effective hunters both day and night. Male lions defend the pride's territory and offspring from "
            "intruders, displaying dominance through roaring, scent marking, and confrontations with rival males."
            " Despite their powerful presence, lions also exhibit playful behaviors, particularly among cubs and "
            "juveniles within the pride. Their role as top predators contributes to ecosystem balance and "
            "biodiversity in African savannahs and grasslands.",

    "zebra": "Zebras are distinctive equids known for their black and white striped coats, making them easily "
             "recognizable in savannah and grassland habitats. They have slender bodies, long legs, and elongated "
             "heads with upright manes. Zebras' coats vary in stripe patterns and intensity, ranging from bold black"
             " and white stripes to lighter shades of brown and cream. These stripes serve as effective camouflage "
             "against predators like lions and hyenas, creating optical illusions and confusion during pursuits. "
             "Zebras are herbivores, feeding primarily on grasses and vegetation, and they are highly adaptable to "
             "various habitats across Africa. They are social animals, often seen in herds led by a dominant stallion"
             " or mare. Zebras use vocalizations, body language, and grooming behaviors for communication and "
             "establishing social bonds within the herd. \n\n"
             "In terms of abilities and strengths, zebras are fast and "
             "agile runners, capable of reaching speeds up to 65 kilometers per hour (40 mph) during sprints. Their "
             "hooves are sturdy and adapted for traversing diverse terrains, including plains, woodlands, and hills. "
             "Zebras also play crucial roles in ecosystems as grazers, shaping vegetation growth, and contributing "
             "to nutrient cycling. Despite their iconic appearance and social dynamics, zebras face threats from "
             "habitat loss, human-wildlife conflicts, and predation, highlighting the importance of conservation "
             "efforts and protected areas for their survival.",

    "kangaroo": "Kangaroos are marsupials native to Australia known for their hopping locomotion, powerful hind "
                "legs, and unique reproductive adaptations. They have muscular bodies, long tails for balance, and "
                "strong hind limbs with large feet adapted for leaping. Kangaroos' front limbs are smaller and used "
                "for grasping and balance while hopping. They are herbivorous, feeding primarily on grasses, leaves,"
                " and plants found in their arid and grassland habitats. Kangaroos are social animals, often seen in "
                "groups called mobs or troops, led by dominant males known as boomers. Female kangaroos, called "
                "flyers or does, carry their young, called joeys, in specialized pouches until they are fully "
                "developed. Kangaroos are adapted to arid environments, capable of conserving water and energy "
                "through specialized physiological mechanisms. \n\n"
                "In terms of abilities and strengths, kangaroos are "
                "excellent hoppers, using their powerful hind legs to cover long distances and evade predators like"
                " dingoes. They can reach speeds up to 56 kilometers per hour (35 mph) in short bursts and sustain "
                "speeds of 20-25 kilometers per hour (12-16 mph) for longer periods. Kangaroos also use their tails"
                " for balance and leverage while hopping. They play essential roles in ecosystems as grazers, "
                "contributing to vegetation control and nutrient cycling. Kangaroos face threats from habitat loss, "
                "climate change, and human activities, highlighting the need for conservation measures and sustainable"
                " management of their habitats.",

    "buffalo": "Buffaloes, also known as African buffalo or Cape buffalo, are large bovids native to Africa known "
               "for their robust build, curved horns, and formidable demeanor. They have massive bodies with thick,"
               " dark coats, large heads, and distinctive horns that curve backward and slightly upward. Buffaloes "
               "are herbivores, feeding primarily on grasses and aquatic plants found in savannahs, grasslands, and "
               "wetlands. They are social animals, often seen in large herds led by dominant females or bulls. "
               "Buffaloes use vocalizations, body language, and scent markings to communicate within the herd and "
               "establish social hierarchies. They are adapted to diverse habitats, including open plains, woodlands,"
               " and marshy areas, and they are excellent swimmers, using water bodies for cooling off, escaping "
               "predators, and accessing new grazing areas. \n\n"
               "In terms of abilities and strengths, buffaloes are "
               "powerful runners and can reach speeds up to 56 kilometers per hour (35 mph) when alarmed or pursued"
               " by predators like lions or hyenas. Their horns are used for defense, territorial displays, and "
               "fighting with rival males during mating seasons. Buffaloes play crucial roles in ecosystems as "
               "grazers, shaping vegetation growth, and providing food and habitat for various species. However, "
               "buffaloes face threats from habitat loss, poaching, and human-wildlife conflicts, emphasizing the "
               "importance of conservation efforts and protected areas for their survival.",

    "beaver": "Beavers are semi-aquatic rodents known for their dam-building behavior, impressive engineering skills,"
              " and adaptations to aquatic habitats. They have stocky bodies, webbed hind feet, and flat, scaly tails,"
              " which they use as rudders while swimming. Beavers have dense fur coats that repel water, keeping them"
              " warm and dry in aquatic environments. They are herbivores, feeding on bark, leaves, aquatic plants,"
              " and roots, and they play crucial roles in shaping wetland ecosystems through their dam construction "
              "activities. Beavers build dams across streams and rivers using logs, branches, and mud, creating ponds"
              " and wetlands that provide habitats for various species. They also construct lodges or burrows within"
              " these water bodies, providing shelter and protection from predators. \n\n"
              "In terms of abilities and "
              "strengths, beavers are skilled builders and engineers, capable of creating complex dam structures "
              "that regulate water flow, prevent flooding, and improve water quality. They are primarily nocturnal,"
              " working on their dams and lodges during the night and foraging for food in the surrounding areas. "
              "Beavers have sharp teeth and powerful jaws adapted for cutting through wood and vegetation, aiding "
              "in their construction activities. They are also known for their strong family bonds, living in family"
              " groups called colonies or lodges. However, beavers face challenges from habitat loss, pollution,"
              " and human activities that disrupt their wetland habitats, highlighting the need for conservation and"
              " management of these critical ecosystems.",

    "donkey": "Donkeys, also known as asses, are domesticated equids known for their hardiness, endurance, and "
              "versatility. They have compact bodies, short legs, and long ears that distinguish them from horses."
              " Donkeys come in various sizes and coat colors, ranging from gray and brown to black and white."
              " They are herbivores, feeding primarily on grasses, hay, and grains, and they have a reputation for "
              "being sure-footed and resilient in challenging terrains. Donkeys have been used by humans for "
              "centuries as working animals, carrying loads, pulling carts, and assisting with agricultural tasks."
              " They are known for their strong bonds with humans and other animals, displaying intelligence, "
              "loyalty, and adaptability. Donkeys have a unique braying vocalization, which varies in tone and "
              "volume depending on their emotions or communication needs. \n\n"
              "In terms of abilities and strengths, "
              "donkeys are excellent pack animals, capable of carrying heavy loads over long distances. Their "
              "sure-footedness and endurance make them suitable for traversing mountainous terrains, deserts, and"
              " rural landscapes. Donkeys are also social animals that thrive in the company of other equids or "
              "companionship with humans. However, they require proper care, including shelter, nutrition, and "
              "veterinary attention, to ensure their well-being and productivity. Donkeys are valued for their "
              "contributions to agriculture, transportation, and therapy programs, serving as reliable partners and"
              " companions in various human activities.",

    "tasmanian devil": "The Tasmanian devil is a unique marsupial native to Tasmania, Australia, known for its "
                       "ferocious temperament, powerful jaws, and distinct behaviors. They have stocky bodies with"
                       " black fur coats, white markings on their chest and shoulders, and a strong odor emitted "
                       "during confrontations or feeding. Tasmanian devils are carnivorous, feeding primarily on "
                       "carrion, small mammals, birds, and reptiles. They have strong jaws and sharp teeth, capable"
                       " of crushing bones and devouring their prey entirely, including fur, bones, and organs. "
                       "Tasmanian devils are solitary animals, except during mating seasons or when competing for"
                       " food sources. They are known for their loud, eerie vocalizations, which include screeches,"
                       " growls, and snarls, often heard during feeding frenzies or territorial disputes. \n\n"
                       "In terms of"
                       " abilities and strengths, Tasmanian devils have powerful senses of smell and hearing, aiding in"
                       " locating food and avoiding predators. They are also skilled climbers, using trees or rocky "
                       "outcrops for shelter, rest, and observation. Tasmanian devils play crucial roles in ecosystems"
                       " as scavengers, helping clean up carrion and prevent the spread of diseases. However, they face"
                       " threats from habitat loss, human encroachment, and a transmissible facial tumor disease that "
                       "has significantly impacted their populations. Conservation efforts, including disease management,"
                       " captive breeding programs, and habitat protection, are essential for the survival of Tasmanian"
                       " devils and the maintenance of healthy ecosystems in Tasmania.",

    "hamster": "Hamsters are small rodents known for their compact size, round bodies, and cheek pouches used for "
               "storing food. They have short legs, fur-covered tails, and whiskers that help them navigate their "
               "environments. Hamsters come in various species and coat colors, including golden, white, gray, and "
               "brown. They are omnivores, feeding on seeds, grains, fruits, vegetables, and occasional insects or"
               " small animals. Hamsters are nocturnal animals, being most active during the night and resting or"
               " sleeping during the day. They are solitary animals, preferring to live alone in burrows or nests "
               "that they construct underground. \n\n"
               "Hamsters are known for their hoarding behavior, collecting and "
               "storing food in their cheek pouches and nest areas for later consumption. They are also adept at "
               "escaping and evading predators, using their agility and speed to navigate obstacles and flee danger."
               " Hamsters have a relatively short lifespan compared to other rodents, typically living 2-3 years in"
               " captivity. They are popular as pets due to their small size, low maintenance requirements, and "
               "entertaining behaviors such as running on exercise wheels and exploring their environments. However,"
               " it's important for hamster owners to provide appropriate habitats, nutrition, and socialization to"
               " ensure the well-being and enrichment of these curious and active rodents.",

    "hawk": "Hawks are predatory birds of prey known for their keen eyesight, powerful talons, and swift hunting "
             "abilities. They belong to the family Accipitridae and are characterized by their sharp, hooked beaks,"
             " strong wings, and aerial hunting techniques. Hawks come in various species, sizes, and plumage colors,"
             " ranging from the red-tailed hawk with its distinctive reddish tail to the sharp-shinned hawk known "
             "for its agile flight and hunting prowess. They are carnivorous, feeding primarily on small mammals,"
             " birds, reptiles, and insects, using their sharp beaks and talons to capture and subdue prey. Hawks"
             " are skilled fliers, using thermal air currents and updrafts to soar high in the sky, scan for prey,"
             " and execute rapid dives or swoops to catch their targets. \n\n"
            "They have exceptional vision, with the "
             "ability to spot prey from great distances and detect subtle movements on the ground. Hawks play "
             "crucial roles in ecosystems as top predators, regulating prey populations and maintaining ecosystem"
             " balance. They are also indicators of environmental health, with declines in hawk populations often"
             " reflecting broader ecological imbalances or habitat degradation. Hawks exhibit territorial behaviors,"
             " establishing and defending nesting territories during breeding seasons. They are also known for "
             "their impressive courtship displays, aerial acrobatics, and vocalizations. Conservation efforts, "
             "including habitat preservation, anti-poaching measures, and education about raptor conservation, are"
             " essential for protecting hawks and ensuring their continued presence in natural ecosystems.",

    "fox": "Foxes are small to medium-sized mammals belonging to the Canidae family, known for their cunning "
           "behavior, adaptability, and bushy tails. They have elongated bodies, pointed muzzles, triangular ears,"
           " and fur coats that vary in color depending on the species and habitat, including red, gray, silver, "
           "and black. Foxes are omnivores, feeding on a diverse diet that includes small mammals, birds, insects,"
           " fruits, vegetables, and carrion. They are highly adaptable to various environments, including forests,"
           " grasslands, mountains, and urban areas, making them one of the most widely distributed carnivores on"
           " Earth. Foxes are solitary animals or live in small family groups called packs, consisting of a mating"
           " pair and their offspring. They use dens for shelter, breeding, and raising young, digging intricate"
           " burrow systems or utilizing natural cavities in the landscape. \n\n"
           "In terms of behaviors and adaptations,"
           " foxes are known for their intelligence, agility, and stealthy hunting techniques. They are skilled"
           " predators, using patience, stalking, and pouncing to catch prey. Foxes are also famous for their"
           " vocalizations, including barks, yips, and high-pitched screams, used for communication within their"
           " species. They have keen senses, including sharp hearing and a strong sense of smell, aiding in"
           " navigation, hunting, and social interactions. Foxes play important roles in ecosystems as mesopredators,"
           " regulating prey populations, scavenging carrion, and contributing to nutrient cycling. However, they"
           " face threats from habitat loss, fragmentation, disease transmission, and human-wildlife conflicts,"
           " necessitating conservation efforts and sustainable management of fox populations and habitats.",

    "hedgehog": "Hedgehogs are small spiny mammals known for their unique defensive mechanism of rolling into a "
                "ball to protect themselves from predators. They belong to the Erinaceidae family and are "
                "characterized by their spiny or prickly coat, stout bodies, and short legs. Hedgehogs have "
                "distinctive snouts, small eyes, and rounded ears, giving them an adorable and curious appearance."
                " They are nocturnal animals, being most active during the night and sleeping in burrows, nests, "
                "or hidden areas during the day. Hedgehogs are omnivores, feeding on a varied diet that includes "
                "insects, worms, small vertebrates, fruits, and vegetation. They use their keen sense of smell "
                "to locate food sources and navigate their environments. \n\n"
                "Hedgehogs are solitary animals, except "
                "during mating seasons or when mothers are caring for their young. They are known for their "
                "defensive behaviors, curling into a tight ball with their spines erect when threatened by "
                "predators. This defense mechanism provides protection for their vulnerable underside and soft "
                "belly. Hedgehogs also have relatively long lifespans for small mammals, often living 3-7 years "
                "in the wild and even longer in captivity with proper care. They are popular as pets due to their"
                " charming appearance, low maintenance requirements, and interesting behaviors such as foraging, "
                "exploring, and burrowing. Hedgehogs play important roles in ecosystems as insectivores, controlling"
                " insect populations and contributing to ecosystem balance. Conservation efforts focus on protecting"
                " hedgehog habitats, reducing human impacts like habitat loss and pollution, and promoting responsible"
                " pet ownership for captive hedgehogs.",

    "horse": "Horses are large, majestic mammals known for their strength, speed, and historical significance in "
             "human cultures worldwide. They belong to the Equidae family and are characterized by their long legs,"
             " muscular bodies, flowing manes and tails, and herbivorous diet. Horses have been domesticated for "
             "thousands of years, serving as modes of transportation, companions in work and sport, and symbols of "
             "status and prestige. They come in various breeds, sizes, colors, and coat patterns, including solid "
             "colors like bay, black, chestnut, and gray, as well as spotted or multi-colored coats. Horses are "
             "herbivores, feeding primarily on grasses, hay, grains, and other plant materials. They have specialized"
             " digestive systems designed for processing fibrous vegetation and extracting nutrients efficiently."
             " Horses are known for their intelligence, sensitivity, and strong social bonds with humans and other "
             "equids. They exhibit complex behaviors, including communication through vocalizations, body language,"
             " and facial expressions. \n\n"
             "In terms of abilities and strengths, horses are powerful runners and jumpers,"
             " capable of reaching speeds up to 55 miles per hour (88 km/h) in short bursts and jumping heights of"
             " over 8 feet (2.4 meters). They have keen senses, including acute vision and hearing, aiding in "
             "navigation, detection of predators, and social interactions. Horses also have strong emotional bonds"
             " with their human handlers or riders, displaying trust, loyalty, and cooperation in various activities."
             " They are utilized in diverse fields such as agriculture, equestrian sports, therapy programs, and "
             "recreational riding. Horse welfare, proper training, and responsible ownership are essential for their"
             " well-being and the success of human-horse partnerships.",

    "kiwi": "Kiwis are unique flightless birds native to New Zealand, known for their small size, long beaks, and "
            "nocturnal habits. They belong to the Apterygidae family and are characterized by their brown or gray "
            "plumage, soft feathers, and distinctive long, slender bills. Kiwis have strong legs and feet adapted "
            "for terrestrial locomotion, including digging for food in forested or grassy habitats. They are "
            "omnivores, feeding on a diet that includes insects, worms, fruits, seeds, and occasionally small "
            "vertebrates. Kiwis are primarily nocturnal, being most active during the night and resting or "
            "hiding during the day to avoid predators. \n\n"
            "They have keen senses of smell and touch, using their "
            "long beaks to probe and extract food from soil, leaf litter, or rotting logs. Kiwis are known for "
            "their unique reproductive biology, with females laying large eggs relative to their body size, and"
            " males taking on the role of incubation and chick rearing. This unusual nesting behavior is rare "
            "among birds and contributes to the conservation challenges faced by kiwi populations. Kiwis play"
            " important roles in New Zealand ecosystems as seed dispersers, insect controllers, and indicators of"
            " forest health. However, they are threatened by habitat loss, introduced predators like stoats and"
            " cats, and human disturbances. Conservation efforts focus on protecting kiwi habitats, predator "
            "control, captive breeding programs, and public awareness to ensure the survival of these iconic and"
            " culturally significant birds.",

    "lizard": "Lizards are a diverse group of reptiles known for their scaly skin, elongated bodies, and ability "
              "to regulate body temperature through external environments. They belong to the order Squamata and"
              " are characterized by their four legs (or absence of legs in some species), tails, and often "
              "colorful or patterned scales. Lizards come in various sizes, from tiny geckos that can fit on a "
              "fingertip to large monitor lizards like the Komodo dragon. They are found in diverse habitats such "
              "as deserts, forests, grasslands, and rocky outcrops, displaying adaptations suited to their "
              "environments. Lizards are ectothermic, meaning they rely on external heat sources to regulate their"
              " body temperatures. They bask in sunlight to warm up and retreat to shade or burrows to cool down."
              " Lizards are carnivorous, omnivorous, or herbivorous, depending on the species, feeding on insects,"
              " small vertebrates, fruits, vegetation, and even nectar in the case of some species like geckos. \n\n"
              " They have keen senses, including vision, smell, and vibration detection, aiding in prey detection,"
              " predator avoidance, and social communication. Lizards use a variety of locomotion methods, including"
              " running, climbing, swimming, and gliding (in some species), showcasing their agility and versatility."
              " They also exhibit diverse reproductive strategies, ranging from egg-laying to live-bearing, depending"
              " on the species. Lizards play important roles in ecosystems as prey for predators, insect controllers,"
              " seed dispersers, and contributors to nutrient cycling through their feeding habits. Conservation "
              "efforts focus on protecting lizard habitats, managing invasive species, and mitigating climate change"
              " impacts on reptile populations.",

    "leopard": "Leopards are powerful and elusive big cats known for their striking coat patterns, stealthy hunting"
               " techniques, and adaptability to various habitats. They belong to the genus Panthera and are "
               "characterized by their golden-yellow fur covered in rosette-shaped spots or patterns. Leopards"
               " have muscular bodies, long tails for balance, and strong jaws equipped with sharp teeth and "
               "powerful muscles for hunting and subduing prey. They are solitary animals, establishing large"
               " territories that they mark with scent markings and vocalizations. Leopards are agile climbers,"
               " using trees, rocks, and elevated vantage points for scouting, resting, and stalking prey. They"
               " are opportunistic carnivores, feeding on a wide range of animals such as antelopes, deer, "
               "monkeys, birds, and occasionally smaller predators like hyenas or jackals. \n\n"
               "Leopards are known"
               " for their stealthy hunting techniques, relying on camouflage, patience, and quick ambushes to"
               " catch their prey. They have keen senses, including sharp vision, acute hearing, and a strong"
               " sense of smell, aiding in nocturnal hunting activities and detection of potential threats."
               " Leopards play crucial roles in ecosystems as top predators, regulating prey populations and"
               " maintaining balanced ecosystems. However, they face threats from habitat loss, human-wildlife"
               " conflicts, poaching for their skins and body parts, and retaliatory killings. Conservation"
               " efforts focus on protecting leopard habitats, reducing human impacts, and promoting coexistence"
               " between leopards and local communities.",

    "koala": "Koalas are iconic marsupials native to Australia known for their cuddly appearance, arboreal lifestyle,"
             " and specialized diet of eucalyptus leaves. They belong to the family Phascolarctidae and are "
             "characterized by their fluffy gray fur, large round ears, broad noses, and bushy tails. Koalas have"
             " strong limbs adapted for climbing and gripping tree branches, along with sharp claws for grasping "
             "foliage. They are primarily nocturnal and spend most of their time resting or sleeping in eucalyptus"
             " trees, which provide both food and shelter. Koalas are herbivores, feeding exclusively on eucalyptus"
             " leaves, which are high in fiber and low in nutrition, requiring koalas to conserve energy and limit"
             " activity. They have specialized digestive systems with long intestines and unique gut bacteria that"
             " help break down eucalyptus toxins and extract nutrients from the leaves. Koalas are solitary animals,"
             " except during mating seasons or when females are caring for their young in pouches. They are known"
             " for their vocalizations, including bellows, grunts, and screams, used for communication, territory"
             " marking, and mate attraction. \n\n"
             "In terms of conservation status, koalas face threats from habitat loss,"
             " urban development, climate change, bushfires, and diseases like chlamydia. Conservation efforts focus"
             " on protecting koala habitats, restoring eucalyptus forests, establishing wildlife corridors, and "
             "implementing measures to reduce human impacts on koala populations. Koalas are also cultural symbols"
             " of Australia and important ambassadors for wildlife conservation and ecosystem protection.",

    "lemur": "Lemurs are unique primates endemic to Madagascar and nearby islands, known for their diverse "
             "species, playful behaviors, and distinctive adaptations. They belong to the infraorder Lemuriformes"
             " and are characterized by their large, reflective eyes, fox-like faces, furry bodies, long tails,"
             " and leaping locomotion. Lemurs come in various sizes, from the tiny mouse lemurs to the large "
             "indri lemurs, and they exhibit a wide range of fur colors and patterns. They are arboreal animals,"
             " spending most of their time in trees and using their strong hind legs and grasping hands and feet"
             " to navigate through forest canopies. Lemurs are omnivores, feeding on fruits, leaves, flowers, "
             "insects, small vertebrates, and occasionally nectar or sap. They have keen senses, including acute"
             " hearing and smell, aiding in communication, foraging, and predator detection. Lemurs are social"
             " animals, often living in groups called troops or clans, consisting of related females, males, and"
             " their offspring. They use vocalizations, scent markings, grooming behaviors, and elaborate displays"
             " for communication, bonding, and establishing social hierarchies within the group. \n\n"
             "In terms of "
             "conservation status, lemurs face significant threats from habitat loss due to deforestation, human"
             " encroachment, illegal logging, and climate change. Conservation efforts focus on protecting lemur"
             " habitats, establishing protected areas, promoting sustainable forestry practices, and raising"
             " awareness about the importance of preserving Madagascar's unique biodiversity.",

    "mole": "Moles are small, fossorial mammals known for their subterranean lifestyle, specialized adaptations"
            " for digging, and unique anatomical features. They belong to the family Talpidae and are characterized"
            " by their cylindrical bodies, velvety fur, tiny eyes, and powerful forelimbs with shovel-shaped hands."
            " Moles have adapted to underground environments, where they create elaborate tunnel systems for "
            "foraging, nesting, and escaping predators. They are insectivores, feeding primarily on earthworms,"
            " insects, larvae, and underground invertebrates, using their sensitive snouts and whiskers to detect"
            " prey in soil and tunnels. Moles have strong muscles and bone structures designed for digging, with "
            "forelimbs specialized for pushing and clearing soil while tunneling.\n\n"
            " They are solitary animals, except"
            " during mating seasons or when mothers are caring for their young in underground burrows. Moles are"
            " known for their efficient digging behaviors, creating molehills or surface ridges as they excavate soil"
            " and search for food. They also play important roles in ecosystems by aerating soil, controlling insect"
            " populations, and contributing to nutrient cycling. However, moles can sometimes be considered pests"
            " when their tunneling activities disrupt gardens, lawns, or agricultural fields. Conservation efforts"
            " focus on understanding mole ecology, minimizing human-mole conflicts, and implementing humane methods"
            " for managing mole populations in urban and rural landscapes.",

    "panther": "Panther is a term used to describe melanistic variants of big cat species, including leopards,"
               " jaguars, and cougars, with black or dark brown fur due to a genetic mutation called melanism."
               " Panthers are not a distinct species but rather color variants of their respective big cat species."
               " They share the same physical characteristics, behaviors, and habitats as their non-melanistic"
               " counterparts, with the main difference being their coat color. Panthers have muscular bodies, sharp"
               " claws, powerful jaws, and keen senses, making them apex predators in their ecosystems. They are"
               " stealthy hunters, relying on camouflage, patience, and ambushes to catch their prey. Panthers are"
               " primarily carnivorous, feeding on a variety of animals such as deer, wild boar, small mammals,"
               " birds, and reptiles. \n\n"
               "They are solitary animals, establishing large territories that they mark with"
               " scent markings and vocalizations. Panthers play crucial roles in ecosystems as top predators,"
               " regulating prey populations and maintaining balanced ecosystems. However, they face threats from"
               " habitat loss, human-wildlife conflicts, poaching, and retaliatory killings. Conservation efforts"
               " focus on protecting panther habitats, reducing human impacts, mitigating conflicts, and promoting"
               " coexistence between panthers and local communities.",

    "pig": "Pigs, also known as domestic pigs or swine, are intelligent, social mammals domesticated for food"
           " production, companionship, and various agricultural purposes. They belong to the Suidae family and"
           " are characterized by their stout bodies, short legs, bristly hair, snouts, and omnivorous diet. Pigs"
           " come in various breeds, sizes, colors, and coat patterns, with some breeds bred specifically for meat"
           " production, while others are raised for their intelligence or as pets. They are highly adaptable animals,"
           " thriving in diverse environments such as farms, forests, and even urban settings. Pigs are omnivores,"
           " feeding on a wide range of foods, including grains, vegetables, fruits, roots, insects, small animals,"
           " and even carrion. They have specialized digestive systems capable of efficiently processing complex"
           " carbohydrates and extracting nutrients from fibrous plant materials. Pigs are known for their social"
           " behaviors, forming strong bonds within social groups called sounders, consisting of related females,"
           " their offspring, and occasionally adult males.  \n\n"
           " They communicate through vocalizations, body language,"
           " and tactile interactions, displaying emotions such as happiness, fear, and distress. Pigs are also"
           " highly intelligent animals, demonstrating problem-solving skills, memory retention, and learning"
           " capabilities comparable to dogs. They have been trained for tasks such as search and rescue, truffle"
           " hunting, and even artistic performances. In agriculture, pigs are raised for meat production (pork),"
           " with various husbandry practices and management systems used worldwide. Conservation efforts focus on"
           " promoting sustainable pig farming practices, welfare standards, and genetic diversity to ensure the"
           " health and well-being of pig populations and meet global food demands.",

    "penguin": "Penguins are flightless birds native to the Southern Hemisphere, known for their aquatic adaptations,"
               " social behaviors, and distinctive black-and-white plumage. They belong to the family Spheniscidae"
               " and are highly adapted for life in the water, with streamlined bodies, flipper-like wings, and"
               " webbed feet for efficient swimming. Penguins come in various species, sizes, and habitats, ranging"
               " from the iconic Emperor penguins of Antarctica to the Galapagos penguins of warmer climates. They"
               " are carnivorous birds, feeding primarily on fish, squid, krill, and other marine creatures found"
               " in ocean waters. Penguins are excellent swimmers, using their flipper-like wings to propel themselves"
               " underwater at high speeds, allowing them to catch prey and evade predators like seals and sea lions."
               " They are also capable of porpoising, a technique where they leap in and out of the water to travel"
               " quickly and breathe efficiently. \n\n"
               "Penguins are highly social animals, forming colonies or rookeries"
               " during breeding seasons, where they engage in courtship displays, nest building, and chick rearing."
               " They use vocalizations, body postures, and visual cues for communication within the colony and to"
               " recognize mates or offspring. Penguins have unique adaptations for surviving in cold environments,"
               " including dense plumage for insulation, counter-current heat exchange in their legs to conserve body"
               " heat, and adaptations for reducing heat loss while swimming. Conservation efforts focus on protecting"
               " penguin habitats, addressing threats such as climate change, overfishing, pollution, and human"
               " disturbances, and promoting sustainable fisheries practices to ensure the survival of penguin"
               " populations and their marine ecosystems.",

    "platypus": "The platypus is a unique monotreme mammal native to Australia, known for its duck-billed appearance,"
                " webbed feet, and egg-laying reproductive strategy. It belongs to the family Ornithorhynchidae and"
                " is characterized by its furry body, beaver-like tail, otter-like feet, and venomous spurs on its"
                " hind limbs (males only). The platypus is one of the few venomous mammals, with venom used primarily"
                " during mating season or territorial disputes. Platypuses are semi-aquatic animals, spending much of"
                " their time in freshwater habitats such as rivers, streams, and lakes, where they forage for food and"
                " build burrows for shelter. They are carnivorous, feeding primarily on aquatic invertebrates such as"
                " insects, crustaceans, and small fish, using their sensitive bills to detect prey in murky waters."
                " \n\n"
                "Platypuses have unique adaptations for underwater foraging, including electroreception, where they"
                " detect electrical signals produced by prey, and specialized cheek pouches for storing food while"
                " underwater. They are excellent swimmers, using their webbed feet and paddle-like tail for propulsion"
                " and maneuverability. Platypuses are nocturnal or crepuscular, being most active during dawn and dusk"
                " hours and resting in burrows during the day. They are solitary animals except during breeding seasons"
                " or when mothers are caring for their young in burrow nests. Platypuses are iconic symbols of Australian"
                " wildlife and face threats from habitat loss, pollution, invasive species, and human activities. "
                "Conservation efforts focus on protecting platypus habitats, implementing water quality regulations,"
                " and conducting research to understand their ecology, behavior, and conservation needs.",

    "pelican": "Pelicans are large water birds belonging to the family Pelecanidae, known for their long bills,"
               " expansive throat pouches, and impressive diving and fishing abilities. They are found on every"
               " continent except Antarctica, inhabiting coastal and inland waters such as oceans, lakes, rivers,"
               " and estuaries. Pelicans come in various species, with the great white pelican, brown pelican,"
               " and Australian pelican being among the most well-known. They are characterized by their long wings,"
               " webbed feet, and large, broad bills with a stretchable pouch used for catching and storing fish."
               " Pelicans are carnivorous birds, feeding primarily on fish, crustaceans, and occasionally small birds"
               " or mammals. They are skilled flyers, using thermal currents, updrafts, and gliding techniques to"
               " cover long distances during migrations or foraging trips. \n\n"
               "Pelicans are known for their group fishing"
               " behaviors, where they cooperatively herd fish into shallow waters or encircle schools of fish before"
               " scooping them up with their bills and pouches. They are also capable of plunge diving from great"
               " heights to catch prey underwater. Pelicans are social birds, often seen roosting or nesting in large"
               " colonies, engaging in courtship displays, vocalizations, and territorial behaviors. They play important"
               " roles in ecosystems as top predators of aquatic environments, helping control fish populations and"
               " contributing to nutrient cycling through their feeding habits. However, pelicans face threats from"
               " habitat loss, pollution, human disturbances, and entanglement in fishing gear. Conservation efforts"
               " focus on protecting pelican habitats, establishing marine protected areas, reducing plastic pollution,"
               " and promoting sustainable fishing practices to ensure the conservation of pelican populations and"
               " marine ecosystems.",

    "orangutan": "Orangutans are large, arboreal apes native to the rainforests of Borneo and Sumatra, known for"
                 " their intelligence, dexterity, and close genetic relationship to humans. They belong to the genus"
                 " Pongo and are characterized by their long arms, shaggy reddish-brown fur, distinctive cheek pads,"
                 " and remarkable tool-use abilities. Orangutans are primarily solitary animals, except during mating"
                 " seasons or when mothers are caring for their offspring. They are herbivorous, feeding primarily on"
                 " fruits, leaves, bark, insects, and occasionally small vertebrates found in forest environments. "
                 "Orangutans are excellent climbers and spend most of their time in trees, using their strong arms and"
                 " grasping hands and feet to navigate through dense canopy layers. They have large brains relative to"
                 " their body size, exhibiting complex cognitive abilities, problem-solving skills, and cultural behaviors"
                 " such as using tools, creating nests, and communicating through vocalizations and gestures. \n\n"
                 "Orangutans"
                 " are highly endangered due to habitat loss, deforestation, illegal hunting, and human-wildlife conflicts."
                 " Conservation efforts focus on protecting orangutan habitats, establishing sanctuaries and protected"
                 " areas, promoting sustainable forestry practices, and raising awareness about the importance of"
                 " conserving these critically endangered great apes. Orangutans are flagship species for rainforest"
                 " conservation, symbolizing the need to protect biodiversity, ecosystems, and the interconnectedness of"
                 " all living beings.",

    "polar bear": "Polar bears are iconic apex predators native to the Arctic region, known for their massive size,"
                  " white fur, powerful swimming abilities, and reliance on sea ice for hunting and habitat. They"
                  " belong to the Ursidae family and are the largest terrestrial carnivores, adapted for life in"
                  " icy environments. Polar bears have thick layers of insulating fur, dense undercoats, and a"
                  " thick layer of blubber that helps them retain heat and buoyancy in frigid waters. They have"
                  " large, strong limbs with partially webbed paws for efficient swimming, and they can cover"
                  " long distances across ice floes in search of prey such as seals, walruses, and occasionally"
                  " whales or carcasses. \n\n "
                  "Polar bears are opportunistic feeders, using their keen sense of smell"
                  " to detect seals' breathing holes or scent trails over long distances. They are skilled hunters,"
                  " using stalking, waiting, and ambush techniques near seal breathing holes or haul-out sites."
                  " Polar bears are excellent swimmers, capable of swimming long distances in search of food or"
                  " suitable ice habitats. They are also known for their curious and intelligent behaviors, "
                  "including playfulness, problem-solving, and social interactions. Polar bears face significant"
                  " threats from climate change, as melting sea ice reduces their hunting grounds, disrupts their"
                  " natural behaviors, and increases human-bear conflicts. Conservation efforts focus on mitigating"
                  " climate change impacts, reducing human disturbances in polar bear habitats, implementing"
                  " sustainable hunting practices with indigenous communities, and conducting research to understand"
                  " polar bear ecology and conservation needs.",

    "rabbit": "Rabbits are small mammals belonging to the family Leporidae, known for their long ears, hopping"
              " locomotion, and rapid reproductive rates. They come in various species, including domesticated"
              " rabbits and wild cottontail rabbits, hares, and pikas. Rabbits are herbivores, feeding primarily"
              " on grasses, clover, vegetables, and other plant materials. They have specialized digestive systems"
              " capable of processing fibrous vegetation and extracting nutrients efficiently. Rabbits are known"
              " for their agility, speed, and keen senses, including excellent vision and hearing, aiding in"
              " predator detection and escape behaviors. They use burrows or warrens for shelter, nesting, and"
              " raising their young, creating elaborate underground tunnel systems for protection. Rabbits are"
              " social animals, often living in groups or colonies, exhibiting behaviors such as grooming, "
              "communication through vocalizations and body language, and cooperative defense against predators."
              " They are prolific breeders, with short gestation periods and large litters, allowing them to"
              " rapidly populate suitable habitats. \n\n"
              "Rabbits play important roles in ecosystems as prey for"
              " predators, contributors to soil health through grazing and burrowing activities, and seed"
              " dispersers for certain plant species. However, they can also be considered pests in agricultural"
              " settings due to their feeding habits and reproductive rates. Conservation efforts focus on"
              " managing rabbit populations in balance with ecosystems, protecting rabbit habitats, and"
              " implementing strategies for reducing human-wildlife conflicts.",

    "sloth": "Sloths are slow-moving, arboreal mammals native to Central and South America, known for their"
             " relaxed lifestyle, long claws, and unique adaptations for life in tree canopies. They belong to"
             " the families Megalonychidae and Bradypodidae and are characterized by their furry bodies, slow"
             " metabolism, and specialized limb anatomy. Sloths have long limbs and curved claws, which they use"
             " to hang upside down from branches and move slowly while conserving energy. They spend the majority"
             " of their time resting or sleeping in trees, feeding on leaves, buds, and fruits found in their"
             " forest habitats. Sloths are herbivores with a low-calorie diet, requiring them to minimize energy"
             " expenditure and maintain a slow pace of life. They have specialized stomachs with multiple chambers"
             " for digesting tough plant materials and extracting nutrients efficiently. Sloths are known for their"
             " slow movements, often taking several minutes to climb a short distance or perform basic activities."
             " They have excellent camouflage in forest environments, blending in with tree foliage and avoiding"
             " detection by predators such as eagles, jaguars, and snakes. \n\n"
             "Sloths are primarily solitary animals,"
             " except during mating seasons or when females are caring for their young. They communicate through"
             " soft vocalizations, body postures, and chemical signals. Sloths play important roles in ecosystems as"
             " seed dispersers, contributors to nutrient cycling through their feces, and hosts for specialized"
             " algae and insects. However, they face threats from habitat loss, deforestation, road mortality,"
             " and illegal wildlife trade. Conservation efforts focus on protecting sloth habitats, establishing"
             " wildlife corridors, educating communities about sloth conservation, and rehabilitating injured or"
             " orphaned sloths for release into the wild.",

    "seagull": "Seagulls, often referred to as gulls, are seabirds belonging to the family Laridae, known for their"
               " adaptability, scavenging behaviors, and aerial agility. They are found in coastal and inland"
               " environments worldwide, ranging from beaches and cliffs to urban areas and garbage dumps. Seagulls"
               " have varying sizes, plumage colors, and adaptations based on their habitats and feeding preferences."
               " They are opportunistic omnivores, feeding on fish, crustaceans, insects, small mammals, carrion,"
               " garbage, and human food scraps. Seagulls are adept fliers, using thermal updrafts, sea breezes,"
               " and wind currents to soar, hover, and glide effortlessly over water and land. They have strong"
               " wings, webbed feet, and sharp beaks adapted for catching and consuming a wide range of prey items."
               " \n\n"
               "Seagulls are highly social birds, often seen in large flocks or colonies, engaging in courtship"
               " displays, vocalizations, and cooperative feeding behaviors. They use calls, postures, and territorial"
               " displays for communication within the group and to establish breeding territories. Seagulls play"
               " important roles in marine and coastal ecosystems as scavengers, cleaners of beaches and shorelines,"
               " and indicators of environmental health. However, they can also become nuisances in urban areas"
               " due to their scavenging behaviors, noise levels, and interactions with humans. Conservation efforts"
               " focus on understanding seagull ecology, managing urban populations, reducing human-wildlife conflicts,"
               " and promoting responsible waste disposal practices to minimize negative impacts on seagull populations"
               " and coastal ecosystems.",

    "red panda": "Red pandas are small arboreal mammals native to the eastern Himalayas and southwestern China,"
                 " known for their distinctive red fur, bushy tails, and bamboo-rich diet. They belong to the family"
                 " Ailuridae and are the only living species in their genus Ailurus. Red pandas have adaptations for"
                 " life in temperate forests, including semi-retractable claws for climbing, dense fur for insulation,"
                 " and a specialized diet primarily consisting of bamboo leaves, shoots, and berries. They are"
                 " herbivorous animals, supplementing their diet with fruits, insects, eggs, and small vertebrates"
                 " when available. \n\n"
                 "Red pandas are solitary and crepuscular, being most active during dawn and dusk"
                 " hours and resting in tree branches or nests during the day. They are agile climbers and spend"
                 " much of their time foraging in trees, using their keen senses of smell and hearing to detect food"
                 " sources and potential threats. Red pandas have a unique pseudo-thumb, an extension of the wrist bone,"
                 " which aids in grasping bamboo and manipulating objects. They communicate through vocalizations,"
                 " scent markings, and body postures, particularly during mating seasons or territorial disputes."
                 " Red pandas are classified as endangered due to habitat loss, fragmentation, poaching, and"
                 " climate change impacts. Conservation efforts focus on protecting red panda habitats, establishing"
                 " wildlife corridors, promoting sustainable forestry practices, and raising awareness about the"
                 " importance of conserving these charismatic and ecologically significant mammals.",

    "snake": "Snakes are elongated, legless reptiles belonging to the order Squamata, known for their"
             " slithering locomotion, predatory behaviors, and diverse adaptations. They are found in"
             " terrestrial, aquatic, and arboreal habitats worldwide, ranging from deserts and grasslands"
             " to forests and wetlands. Snakes come in various species, sizes, colors, and patterns, with"
             " adaptations suited to their environments and feeding strategies. They are carnivorous, feeding"
             " primarily on rodents, birds, insects, fish, amphibians, and other small animals. Snakes have"
             " specialized jaws and teeth for swallowing prey whole or delivering venom in venomous species."
             " Non-venomous snakes rely on constriction to subdue prey, while venomous snakes use venom for"
             " immobilization and digestion. Snakes are ectothermic, meaning they rely on external sources"
             " of heat to regulate their body temperatures, often basking in sunlight or seeking shelter in"
             " warmer environments. They have forked tongues for chemoreception, helping them detect prey,"
             " predators, and potential mates through scent trails.\n\n"
             " Snakes use a combination of visual cues,"
             " vibrations, and heat signatures to locate and capture prey efficiently. They are often"
             " misunderstood and feared due to cultural perceptions and myths, but most snake species are"
             " non-aggressive and play important roles in ecosystems as predators, controlling rodent populations"
             " and contributing to biodiversity. Conservation efforts focus on habitat protection, reducing"
             " human-snake conflicts, combating illegal trade, and promoting snake education and conservation"
             " awareness.",
    "squirrel": "Squirrels are small to medium-sized rodents belonging to the family Sciuridae, known for their"
                " bushy tails, agile movements, and habit of storing food. They are found in various habitats,"
                " including forests, woodlands, urban areas, and parks, across different continents. Squirrels"
                " come in a variety of species, such as tree squirrels, ground squirrels, flying squirrels, and"
                " chipmunks, each adapted to specific environments and lifestyles. They have sharp claws, strong"
                " hind legs for leaping, and excellent balance, allowing them to climb trees, run along branches,"
                " and jump between surfaces with ease. Squirrels are omnivorous, with diets consisting of nuts,"
                " seeds, fruits, insects, eggs, fungi, and occasionally small vertebrates. They are known for their"
                " caching behavior, where they store surplus food in underground burrows or hidden locations to"
                " consume during winter or times of scarcity. \n\n"
                "Squirrels are active during the day (diurnal) and"
                " communicate using vocalizations, tail movements, and scent markings. They build nests, or dreys,"
                " made of twigs, leaves, and other materials, for shelter and raising their young. Squirrels play"
                " important roles in ecosystems as seed dispersers, helping maintain plant diversity and forest"
                " regeneration. They are also prey for various predators, including birds of prey, snakes,"
                " carnivores, and domestic pets. While some squirrel species are abundant and adaptable to human"
                " environments, others face challenges such as habitat loss, fragmentation, and competition with"
                " invasive species. Conservation efforts focus on protecting squirrel habitats, managing urban"
                " populations, and promoting coexistence strategies to minimize conflicts and support squirrel"
                " populations in diverse ecosystems.",

    "turkey": "Turkeys are large birds native to North America, known for their distinctive features such as"
              " fleshy wattles, caruncles, and fan-shaped tails. They belong to the family Phasianidae and are"
              " closely related to grouse, pheasants, and other game birds. Turkeys come in two primary species:"
              " the wild turkey (Meleagris gallopavo) and the domesticated turkey (Meleagris gallopavo domestica)."
              " Wild turkeys are known for their iridescent plumage, metallic hues, and robust build, while domestic"
              " turkeys are selectively bred for meat production and may have different color variations and"
              " characteristics. Turkeys are omnivores, feeding on a variety of foods such as seeds, nuts, fruits,"
              " insects, small vertebrates, and plant matter. They have powerful legs and strong beaks adapted"
              " for foraging, scratching the ground, and pecking at food items. Turkeys are social birds, often"
              " forming flocks or groups called rafter, particularly during feeding and roosting times. They"
              " communicate through vocalizations, including gobbles, clucks, purrs, and alarm calls, used for"
              " signaling group movements, threats, or courtship displays. \n\n"
              "Turkeys play important roles in"
              " ecosystems as seed dispersers, insect controllers, and contributors to nutrient cycling through"
              " their foraging activities. They are also culturally significant birds, associated with Thanksgiving"
              " celebrations in the United States and traditional hunting practices in various cultures. While"
              " wild turkey populations have rebounded due to conservation efforts, some challenges remain,"
              " including habitat loss, predation, hunting pressures, and diseases. Conservation programs focus"
              " on sustainable turkey management, habitat restoration, hunting regulations, and public education"
              " to ensure the conservation of wild turkey populations and their habitats.",

    "wolf": "Wolves are iconic carnivores belonging to the Canidae family, known for their social structures,"
            " hunting prowess, and ecological roles as apex predators. They are found in diverse habitats"
            " across North America, Eurasia, and parts of Africa, ranging from forests and tundra to grasslands"
            " and mountains. Wolves come in several subspecies, such as gray wolves, red wolves, arctic wolves,"
            " and Ethiopian wolves, each adapted to specific environments and prey species. They have muscular"
            " bodies, bushy tails, keen senses, and a range of vocalizations for communication within packs."
            " Wolves are highly social animals, living in family groups called packs, consisting of alpha, beta,"
            " and subordinate members with defined roles in hunting, territory defense, and pup rearing. They"
            " communicate through howls, barks, growls, and body postures, coordinating pack activities and"
            " maintaining social cohesion. \n\n"
            "Wolves are opportunistic carnivores, feeding on ungulates such as"
            " deer, elk, moose, and caribou, as well as small mammals, birds, fish, and carrion. They are"
            " skilled hunters, using cooperative strategies, stalking, chasing, and ambush tactics to catch prey."
            " Wolves play crucial roles in ecosystems by regulating prey populations, shaping vegetation dynamics,"
            " and creating cascading effects on other wildlife species. They are also culturally significant"
            " animals, symbolizing wilderness, resilience, and complex social behaviors. Despite their ecological"
            " importance, wolves face threats such as habitat loss, human-wolf conflicts, poaching, and diseases."
            " Conservation efforts focus on wolf recovery programs, habitat conservation, predator-prey dynamics,"
            " and public awareness to promote coexistence between wolves and human communities while ensuring"
            " healthy ecosystems.",

    "wombat": "Wombats are burrowing marsupials native to Australia, known for their sturdy build, short legs,"
              " and rodent-like appearance. They belong to the family Vombatidae and are herbivorous mammals"
              " adapted for life in various habitats, including forests, grasslands, and semi-arid regions."
              " Wombats come in three species: the common wombat (Vombatus ursinus), southern hairy-nosed wombat"
              " (Lasiorhinus latifrons), and northern hairy-nosed wombat (Lasiorhinus krefftii), each with"
              " distinct characteristics and distributions. Wombats have robust skulls, strong teeth for chewing"
              " tough vegetation, and powerful forelimbs equipped with long claws for digging burrows and tunnels."
              " They are primarily nocturnal or crepuscular, being most active during dawn and dusk hours and"
              " resting in burrows during the day to avoid heat and predators. Wombats are solitary animals,"
              " maintaining territories marked with scent glands and communicating through vocalizations and"
              " body language. They are herbivores, feeding on grasses, roots, tubers, and bark, using their"
              " sensitive noses to detect food sources and potential threats.\n\n"
              " Wombats are excellent diggers,"
              " creating extensive burrow systems with multiple entrances, chambers for resting, nesting, and"
              " raising their young. They are well adapted for burrow life, with backward-facing pouches to"
              " prevent soil from entering while digging. Wombats also exhibit behaviors such as wallowing in"
              " mud or water to cool off, marking territories with feces, and grooming their fur for hygiene."
              " While wombats are generally slow-moving and placid, they can defend themselves aggressively"
              " when threatened, using their strong legs and sharp claws for defense. Conservation efforts focus"
              " on protecting wombat habitats, managing human-wombat conflicts, preventing road accidents, and"
              " addressing threats such as habitat loss, predation by introduced species, and diseases like mange."
              " Public education and awareness campaigns also play a crucial role in promoting wombat conservation"
              " and appreciation."
}

# Function to display details of a selected animal
def show_animal_details(animal):
    # Create a new window for animal details
    detail_window = tk.Toplevel()
    detail_window.title(animal.capitalize())
    detail_window.geometry("800x600")
    detail_window.configure(bg="white")

    # Create a canvas and scrollbar for the detail window
    canvas = tk.Canvas(detail_window, bg="white")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar = tk.Scrollbar(detail_window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame to hold the details
    detail_frame = tk.Frame(canvas, bg="white")
    canvas.create_window((0, 0), window=detail_frame, anchor='nw')

    # Add a title label with the animal name
    title_label = tk.Label(detail_frame, text=animal.capitalize(), font=("Helvetica", 24, "bold"), bg="white")
    title_label.pack(pady=20)

    # Try to load and display the animal image
    try:
        animal_image = Image.open(f"Images/easy/{animal.lower()}.jpg")
        animal_image = resize_image(animal_image, 400, 400)
        animal_photo = ImageTk.PhotoImage(animal_image)
        image_label = tk.Label(detail_frame, image=animal_photo, bg="white")
        image_label.image = animal_photo  # Keep a reference to avoid garbage collection
        image_label.pack(pady=20)
    except FileNotFoundError:
        image_label = tk.Label(detail_frame, text="Image not available", font=("Helvetica", 18), bg="white")
        image_label.pack(pady=20)

    # Add a description label with the animal description
    description = animal_descriptions.get(animal.lower(), "Description not available.")
    description_label = tk.Label(detail_frame, text=description, font=("Helvetica", 18), wraplength=760,
                                 justify="left", bg="white")
    description_label.pack(pady=20)

    # Update the scroll region to include the new frame size
    detail_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    # Function to handle mouse wheel scrolling
    def _on_mouse_wheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    detail_window.bind_all("<MouseWheel>", _on_mouse_wheel)
    detail_window.bind_all("<Button-4>", _on_mouse_wheel)
    detail_window.bind_all("<Button-5>", _on_mouse_wheel)

# Function to search for animals in the list based on user input
def search_animal(event, search_entry, search_listbox, error_label):
    """Searches for animals based on the user's input."""
    search_term = search_entry.get().lower()
    matching_animals = [animal for animal in animal_list if search_term in animal.lower()]
    search_listbox.delete(0, tk.END)
    if matching_animals:
        error_label.config(text="")
        for animal in matching_animals:
            search_listbox.insert(tk.END, animal)
    else:
        error_label.config(text="No matching animal found. Please try again.", fg="red")

# Function to perform search when search button is clicked
def perform_search(search_entry, search_listbox, error_label):
    search_term = search_entry.get().strip().title()
    if search_term in animal_list:
        error_label.config(text="")
        show_animal_details(search_term)
    else:
        error_label.config(text="No matching animal found. Please try again.", fg="red")

# Function to open the main learning window
def open_learn(root):
    root.title("Learn about Animals")
    root.geometry("800x600")
    root.configure(bg="white")

    # Add a title label
    title_label = tk.Label(root, text="Learn about Animals", font=("Helvetica", 24, "bold"), bg="white")
    title_label.pack(pady=20)

    # Create a frame for the search bar
    search_frame = tk.Frame(root, bg="white")
    search_frame.pack(pady=20)

    # Add a label and entry for the search bar
    search_label = tk.Label(search_frame, text="Search Animal:", font=("Helvetica", 18), bg="white")
    search_label.pack(side=tk.LEFT, padx=5)
    search_entry = tk.Entry(search_frame, font=("Helvetica", 18))
    search_entry.pack(side=tk.LEFT, padx=5)

    # Add a search button
    search_button = tk.Button(search_frame, text="Search", font=("Helvetica", 18), command=lambda: perform_search(search_entry, search_listbox, error_label))
    search_button.pack(side=tk.LEFT, padx=5)

    # Create a listbox to display the search results
    search_listbox = tk.Listbox(root, font=("Helvetica", 18))
    search_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

    # Create an error label to display search errors
    error_label = tk.Label(root, text="", font=("Helvetica", 18), fg="red", bg="white")
    error_label.pack(pady=10)

    # Bind the search function to the search entry
    search_entry.bind("<KeyRelease>", lambda event: search_animal(event, search_entry, search_listbox, error_label))

    # Populate the listbox with the initial animal list
    for animal in animal_list:
        search_listbox.insert(tk.END, animal)

    # Bind the listbox selection to show animal details
    search_listbox.bind('<<ListboxSelect>>', lambda event: show_animal_details(search_listbox.get(search_listbox.curselection())))

# Function to resize an image while maintaining its aspect ratio
def resize_image(image, max_width, max_height):
    w, h = image.size
    ratio = min(max_width / w, max_height / h)
    new_size = (int(w * ratio), int(h * ratio))
    return image.resize(new_size, Image.Resampling.LANCZOS)

# Main program entry point
if __name__ == "__main__":
    root = tk.Tk()
    open_learn(root)
    root.mainloop()
