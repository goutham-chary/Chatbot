from voice_engine import say
import sys
import random

def check_command(command, app):
    greetings = ["hi", "hai", 'hiiii' "how are you", "is anyone there", "hello", "what's up how are you", "hey"]
    goodbye = ["see you", "see you later", "bye bye", "iam leaving", "bye", "talk to you later", "i got to go"]
    mlr = ["tell me about mlrit", "give me the information about mlrit", "history of MLRIT", "when was mlrit founded?",
           "about MLRIT", "ranking of MLRIT", "rank of this collge", "significance of MLRIT", "significance of MLR",
           "significance of this college", "founded by whom", "founder of MLRIT", "founder of MLR"]
    course = ["list of courses", "list of courses offered", "list of courses offered in MLRIT",
              "what are the courses offered in MLRIT", "courses?", "courses offered", "courses you offer",
              "courses in MLRIT", "branches?", "courses available in MLRIT", "branches available in MLR",
              "what are the courses in MLRIT", "branches available in MLR",
              "can you tell me the branches available in MLR", "can you tell me the courses available in MLR",
              "different branches ", "different courses", "branches available ",
              "different departments available in MLR", "different departments available",
              "certification courses offered", "certification course", "training", "training programs",
              "special training "]
    admissions = ["what is the admission process of MLRIT", "admission proess", "admit process",
                  "HOW TO GET SEAT IN COLLEGE", "seat", "seat in college", "nri category", "EAMCET", "mains",
                  "how can i get into MLRIT", "getting into MLRIT", "get seat in college",
                  "what is the process of admission ", "what is the admission process",
                  "how to take admission in your college", "what is the process for admission", "admission",
                  "admission process", "process to admit", "admit in college?"]
    name = ["name", "your name", "do you have a name", "what are you called", "what is your name",
            "what should i called you", "what are you", "who are you", "who is this", "whom iam chatting with",
            "who am i talking to"]
    hours = ["timing of college", "what is timing of college", "working days", "when are you guys open",
             "what are your hours", "hours of operation", "when will the college open", "college timing",
             "what about college timing", "is college open on saturday", "tell something about college timing",
             "what is the college hours", "when should i come to college", "when is my college timing",
             "timing college"]
    cse_hod = ["who is the hod of cse department", "cse  department hod", "hod of cse department", "hod cse department",
               "who is the head of department of cse department ", "what is cse hod name"]
    ece_hod = ["who is the hod of ece department", "ece  department hod", "hod of ece department", "hod ece department",
               "who is the head of department of ece department ", "what is ece hod name"]
    areo_hod = ["who is the hod of Aeronotical department", "Aeronotical  department hod",
                "hod of Aeronotical department", "hod Aeronotical department",
                "who is the head of department of Aeronotical department ", "what is Aeronotical hod name"]
    it_hod = ["who is the hod of IT department", "IT  department hod", "hod of IT department", "hod IT department",
              "who is the head of department of IT department ", "what is IT hod name"]
    mech_hod = ["who is the hod of mechanical department", "mechanical  department hod", "hod of mechanical department",
                "hod mechanical department", "who is the head of department of mechanical department ",
                "what is mechanical hod name"]
    eee_hod = ["who is the hod of EEE  department", "EEE   department hod", "hod of EEE  department",
               "hod EEE  department", "who is the head of department of EEE  department ", "what is EEE  hod name"]
    fd_hod = ["who is the hod of first year department", "first year   department hod", "hod of first year  department",
              "hod first year department", "who is the head of department of first year  department ",
              "what is first year  hod name"]
    mba_hod = ["mba hod","who is the hod of mba department", "mba   department hod", "hod of mba  department",
               "hod mba department", "who is the head of department of mba department ", "what is mba  hod name"]
    number = ["info", "contact info", "info number", "more info", "how to contact college", "contact number",
              "college number", "how to contact you", "can i get your contact number", "how to call you",
              "phone number", "phone no", "call no", "call"]
    clubs = ["what are different clubs in MLRIT", "clubs in MLRIT", "what are extra curricular activities in MLRIT",
             "clubs", "how many clubs does MLRIT have", "how many clubs are there in college",
             "what are the clubs in MLRIT", "how many clubs does college have", "are there any clubs", "creative arts"]
    certification = ["what about certification", 'certificate']
    itorcse = ["what is the difference between IT and CSE", "which is preferrable better IT or CSE",
               "how do they teach in IT", "how do they teach in CSE", "IT or CSE",
               "which branch do companies prefer IT or CSE", "about IT and CSE", "IT vs CSE what to choose",
               "IT vs CSE which is better", "IT vs CSE"]
    fees = ['fee', "what about the fees structure ", "what about the fees structure in MLRIT", "information about fees",
            "information on fees", "tell me the fee", "college fee", "fees per semester",
            "what is the fee of each year", "what is the fee", "fees for first year", "fees",
            "tell me something about fees", "fees details"]
    g_council = ["who are the members of governing council in MLRIT", "members of governing council",
                 "governing council", "governing council members", "does the college have governing council",
                 "mlrit governign council"]
    hostel = ["hostel facility", "hostel details ", "hostel fees", "hostel address", "hostel facilities",
              "does college provide hostel", "where is college hostel", "do you have hostel", "do you guys have hostel",
              "hostel", "hostel capacity", "what is hostel fee", "how to get into hostel",
              "how far is hostel form college", "how big is teh hostel", "hostel guide"]
    events = ["events organized", "List of events", "fests in college", "fests", "technical fest", "cultural fest",
              "does mlrit have fests", "list of events organized in mlrit", "list of events conducted in mlrit",
              "what events are conducted in college", "are there any events held in mlrit", "events?", "functions",
              "what are the events", "tell me about events", "what about event"]
    syllabus = ["what is engineering syllbus", "what is syllbus", "what is the timetable", "timetable", "syllabus",
                "how do they teach in cse", "how can i know the time table"]
    library = ["what about library", "where is library", "library is good or not", "library", "how many libraries",
               "tell me about library"]
    canteen = ["food facilities", "canteen food", "canteen facility", "cafetaria ", "menu", "food"]
    ground = ["what about ground", "is the ground good", "cricket ground", "ground"]
    indoor = ['indoor', 'stadium', 'indoor stadium', 'games', 'hockey', 'sports']
    placements = ["placements", "what about placements", "do you have placements"]
    cie = ["is cie  good", "cie ", "what about cie ", "tell me something about cie", "how can i join cie"]
    bunk = ["where can i bunk", "what happens if i caught while bunking", "is it ok to bunk", "perfect place to bunk"]
    blocks = ["which block is cse ", "which block is ece", "which block is mechanical",
              "which block is aero aeronotical", "which block is it", "which block is eee", "which block is csm",
              "which block is cs-it", "which block is aiml", "how many blocks are there in mlrit"]
    att = ["is attendance mandatory", "how much attendance is required to write exams", "attendance"]

    response = x = ""

    if command in greetings:
        response = ["hello", "hi, there how can i help you ", "good to see you"]
        x = random.choice(response)

    elif command in goodbye:
        response = ["sad to see you go ", "talk to you later", "good bye", "come back soon"]
        x = random.choice(response)


    elif command in mlr:
        x = "MARRI LAXMAN REDDY INSTITUTE OF TECHNOLOGY (MLRIT) ia an engineering college in hyderabad. Founded by DR. sri marri laxman reddy garu in the year 2005. which is famous for sports and study .MLR Institute of Technology is known for its integrated curriculum with equal importance to academics, employable skills & sports. MLR Institute of Technology (MLRIT) is located at Dundigal, Hyderabad, Telangana, India. The institution was started in 2005 by the KMR Education Trust, headed by Mr. Marri Laxman Reddy. The Institute has Six UG courses along with Seven PG Courses. The Institute is affiliated with Jawaharlal Nehru Technological University, Hyderabad (JNTUH). It was granted Autonomous status by University Grants Commission (India) in the year 2015.MLRIT is imparting imparting higher education in the fields of Electronics Communication Engineering(ECE),Computer Science Engineering(CSE), Mechanical Engineering(ME),Aeronautical Engineering(AE), Information Technology(IT) ,Master of Business Administration(MBA), Aerospace Engineering, Embedded Systems, Digital Systems and Computer Electronics, Computer Science, Software Engineering, CAD/CAM and Thermal Engineering. "


    elif command in course:
        x = "MLRIT has several courses like  1) C S E, 2) I T,3) CIVIL, 4) EEE, 5) MECHANICAL, 6) E C E, 7) AERONOTICAL,  8) A I M L, 9) DATA SCIENCE, 10) CYBER SECURITY, 11) C S I T   \n additionally ENVIRONMENTAL  SCIENCE to know more about the courses visit https://mlrit.ac.in/campus-life/"


    elif command in admissions:
        x = "A student can get admit in MLRIT in these ways 1) EAMCET 2)from polytechnic 3)Donation"


    elif command in name:
        response = ["Iam MLR", "you can call me MLRIT BOT"]
        x = random.choice(response)


    elif command in hours:
        x = "college is open from 9:00 am to 4:10 pm from monday to saturday \n second saturday is holiday"


    elif command in cse_hod:
        response = ["CSE .HOD is Dr A BALARAM gaaru", "the head of cse department is Dr A BALARAM gaaru",
                    "Dr A BALARAM gaaru is the head of cse department and visit https://mlrit.ac.in/computer-science-engineering/ for more details"]
        x = random.choice(response)


    elif command in ece_hod:
        response = ["ece .HOD is Dr. s v s prasad gaaru", "the head of ece department is Dr. s v s prasad gaaru",
                    " Dr. s v s prasad gaaru is the head of ece department and visit https://mlrit.ac.in/ece/ for more details"]
        x = random.choice(response)


    elif command in areo_hod:
        response = ["Aeronotical .HOD is Dr. M satyanaryana gupta gaaru",
                    "the head of Aeronotical department is Dr. M satyanaryana gupta gaaru",
                    " Dr. M satyanaryana gupta gaaru is the head of Aeronotical department and visit https://mlrit.ac.in/aeronautical-engineering/ for more details"]
        x = random.choice(response)


    elif command in it_hod:
        response = ["IT .HOD is Dr. N. V RajaSekhar Reddy gaaru",
                    "the head of IT department is Dr. N. V RajaSekhar Reddy gaaru",
                    " Dr. N. V RajaSekhar Reddy gaaru is the head of IT department and visit https://mlrit.ac.in/it/ for more details"]
        x = random.choice(response)


    elif command in mech_hod:
        response = ["mechanical .HOD is Dr. muhammed anaz khan gaaru",
                    "the head of mechanical department is Dr. muhammed anaz khan gaaru",
                    " Dr. muhammed anaz khan gaaru is the head of mechanical department and visit https://mlrit.ac.in/mechanical-engineering/ for more details"]
        x = random.choice(response)


    elif command in eee_hod:
        response = ["EEE  .HOD is Dr. A. sudhakar gaaru", "the head of EEE  department is Dr. A. sudhakar gaaru",
                    "Dr. A. sudhakar gaaru is the head of EEE  department and visit https://mlrit.ac.in/eee/ for more details"]
        x = random.choice(response)


    elif command in fd_hod:
        response = ["first year  .HOD is Dr. achchi reddy gaaru and Dr.radhika gaaru",
                    "the head of first year  department is Dr. achchi reddy gaaru and Dr.radhika gaaru",
                    "Dr. achchi reddy gaaru and Dr.radhika gaaru is the head of first year department and visit https://mlrit.ac.in/freshman/ for more details"]
        x = random.choice(response)


    elif command in mba_hod:
        response = ["mba  .HOD is Dr. m. v. narasimha rao gaaru",
                    "the head of mba  department is Dr. m. v. narasimha rao gaaru",
                    "Dr. m. v. narasimha rao gaaru is the head of mba department and visit https://mlrit.ac.in/mba/ for more details"]
        x = random.choice(response)


    elif command in number:
        x = "you can contact +91 9652226061 for more information"


    elif command in clubs:
        x = "clubs in MLRIT are 1.came club 2.scope club 3.ewb club 4.club literati 5.mun club 6.code club 7.nss club 8.cie club 9.stm club 10.aim club 11.squad club 12.hacnic club 13.robotics club 14.aero club\nto know morw about the clubs please visit https://mlrit.ac.in/campus-life/"


    elif command in certification:
        x = "to know about certifications visit https://www.mlrit.ac.in"


    elif command in itorcse:
        x = "computer science and engineering deals with the design and development of computer components,whereas \n information technology"


    elif command in fees:
        x = "for fee details visit https://mlrinstitutions.ac.in"


    elif command in g_council:
        x = "for details of all the members of governing council visit https://mlrinstitutions.ac.in"


    elif command in hostel:
        x = "MLRIT have a well designed state of the art of hostel for both boys and girs\n it has a lot of facilities from hostel"


    elif command in events:
        x = "For security reasons, we are not providing information about events here. so, to know about the upcoming events visit https://www.mlrit.ac.in"


    elif command in syllabus:
        x = "To know the syllabus and time table visit https://www.erp.mlrinstitutions.ac.in and login with your credentials"


    elif command in library:
        x = "MLRIT has one library on first floor beside C.I.E \n library timings are 9:00 A.M to 5:30 P.M"


    elif command in canteen:
        x = "MLRIT has a canteen with variety of food items available \n stalls like 1)nescafe 2)pizza hut 3)juice point 4)sarza point are also available "


    elif command in ground:
        x = "MLRIT College also has a Cricket Ground with world class facilities; This ground is equipped with 4 Flood lights which provides a wonderful lighting capacity of 77 Thousand watts to play a Night match also."


    elif command in indoor:
        x = "College has a World class Indoor Stadium built up in an area of more than 26000 sqft with 2 floors both the sides with a beautiful gallery & stadium can accommodate a seating capacity of 1000 people, and equipped with 10 Badminton Courts and Table Tennis Hall which accommodates 20 TT tables. Indoor stadium also has a Gym with latest updated and world class Gym equipments.This stadium has a vast hall which not only accommodates 4 Snooker Tables but also it can accommodate a space of more than 6 carom Boards. This stadium has a space even for squash court. At 2nd floor a massive hall which is dedicated to the sport fencing where champions are made.Indoor stadium also has a space for Zumba hall and a Meditation hall.The best part of the stadium is that it can also provide accommodation with 32 rooms.College has a outdoor games facility with games like, Volley ball (2 courts) , Throwball (1 court) , Basketball (1 court) Kabaddi 2 (Courts) Kho kho field, Football field, Athletic Track."


    elif command in placements:
        x = "MLR Institute of Technology, in its journey of 16 years has become a locus yielding academic excellence, had been consistently achieving 80% and above placements every year in various reputed MNCs across the globe. It emphasizes on identifying the virtues of its students individually and nourishes them accordingly thereby helps them in expanding their intellectual horizons as well as contributes to their overall personality development, ostensibly proving the transformation in the zone a proximal development of every student who joins the institution. The transformation of an amateur engineering student into a self-motivated wizard of versatile domains at the tip of fingers & multi-tasking abilities will be taken care of, by the Training & Placements wing at MLR Institute of Technology."


    elif command in cie:
        x = "MLRIT CIE leads in creating Hyderabad's pioneering innovation and startup eco-system predominantly among student community through our incubation and mentoring programs "


    elif command in bunk:
        x = "Bunking the classes is not allowed in MLRIT. If you caught while bunking the classes , a strict action will be taken against you \n it may lead to suspension of a student, anyway our campus has many cool places to get relaxed in free time"


    elif command in blocks:
        x = "MLRIT have a total of 9 blocks.\n 1.mahatma gandhi block for cse\n2.srinivasa ramanujan block for 3rd years \n3.abdul kalam block for ece \n4.kalpana chawla block for freshman department\n5.mother teresa block for labs \n6.stp block for placement training \n7.vs block for mechanical \n8.jc block for aero"


    elif command in att:
        x = "75% attendance is required to get eligibility to write exams , if not maintained a condontion of 6000 rupees has to be paid to write external exams"

    if command in ['exit', 'quit']:
                say("miss you!", app)
                sys.exit()

    app.ex(x, command)
    say(response, app)