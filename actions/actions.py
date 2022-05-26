
# ---  actions.py  --- #
 


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import pyjokes
from datetime import time


class ActionHelloWord(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispathcer: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text ,Any]]:

        data= [ { "title": "Timetable", "payload": "Show me the timetable" },
                { "title": "Assignments", "payload": "Show me my upcomming assignments" }, 
                { "title": "Grades", "payload": "Show me my grades" }, 
                { "title":"help", "payload": "help"} ]

        message={"payload":"quickReplies","data":data}
        dispathcer.utter_message(text="Hi there! I'm Hose, the uni helper that eases your access to resources. How are you today? :D",json_message=message)
        
        return []


class ActionGuide(Action):

    def name(self) -> Text:
        return "action_guide_quick_ac"

    def run(self, dispathcer: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text ,Any]]:

        data= [ { "title": "Timetable", "payload": "Show me the timetable" },
                { "title": "Assignments", "payload": "Show me my upcomming assignments" }, 
                { "title": "Grades", "payload": "Show me my grades" },
                { "title": "Jokes", "payload": "Tell me a joke" },
                { "title":"help", "payload": "help"} ]

        message={"payload":"quickReplies","data":data}
        dispathcer.utter_message(json_message=message)
        
        return []


class ActionAllActions(Action):

    def name(self) -> Text:
        return "action_all_actions"

    def run(self, dispathcer: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text ,Any]]:

        data= [ { "title":"Timetable", "payload": "Show me the timetable" },
                { "title":"Assignments", "payload": "Show me my upcomming assignments" }, 
                { "title":"Grades", "payload": "Show me my grades" }, 
                { "title":"Extensions", "payload": "I want to apply for an extension"},
                { "title":"Jokes", "payload": "Tell me a joke" },
                { "title":"Module Info", "payload": "What are my modules"},
                { "title":"EEC Handbook", "payload": "EEC Handbook"},
                { "title":"Course Programme", "payload": "Show me the course programme"},
                { "title":"Staff contact", "payload": "Show me my lecturer contact info"},
                { "title":"Videos", "payload": "Show me a video"},
                { "title":"Harry Potter 1", "payload": "Philosopher Stone"},
                { "title":"Harry Potter 2", "payload": "Sorcere's Stone"}, ]

        message={"payload":"quickReplies","data":data}
        dispathcer.utter_message(text="Here is a list of all the quick actions",json_message=message)

        ##dispathcer.utter_message(text="type help if you want to see all the actions I can do!")

        return []


class ActionTimetableDay(Action):

    def name(self) -> Text:
        return "action_ask_timetable_day"

    def run(self, dispathcer: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text ,Any]]:
        
        #startTime = time.time()

        # options = ChromeOptions()
        # options.headless = True
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # s = Service('C:/SeleniumDrivers/chromedriver')

        # driver = webdriver.Chrome(service=s, options=options)

        # driver.get("https://webapp.coventry.ac.uk/Timetable-main/Show/8246819?f=&t=&d=20220225&u=EEC/Timetable&k=Z4ZhqK$x4OdZtHHno$SZIOLrFa0.X#view=agendaWeek");
        # driver.implicitly_wait(30)

        # titles = []
        # details = []
        
        # #find the button that selects the day's calandar and clicks it
        # driver.find_element(by=By.XPATH, value='.//*[@id="calendar"]/table/tbody/tr/td[3]/span[5]').click()
        
        # #the parent element containing all the slots later to be clicked on to reveal the data rich pop-ups
        # parent_elem = driver.find_elements(by=By.XPATH, value=".//div[@class='fc-event fc-event-vert fc-event-start fc-event-end']")

        
        # for b in range(1, len(parent_elem)+1):
        #     try:
        #         #open the box
        #         div = driver.find_element(by=By.XPATH,value=f'.//*[@id="calendar"]/div/div/div/div[3]/div/div/div[{b}]').click()

        #         #title div
        #         someDiv = driver.find_element(by=By.XPATH, value='.//div[@class="ui-dialog-titlebar ui-widget-header ui-corner-all ui-helper-clearfix"]')
        #         title = someDiv.text
        #         titleFin = title.replace('\n', '').replace('close','')

        #         #details div
        #         someOtherDiv = driver.find_element(by=By.XPATH, value='//div[@id="popup"]')
        #         detail = someOtherDiv.text
  
        #         dispathcer.utter_message(text=f"{titleFin}{detail}")

  
        #         #close the box
        #         driver.find_element(by=By.XPATH, value='//span[@class="ui-icon ui-icon-closethick"]').click()

        #     except:
        #         break
                    
        # driver.quit()
        
        #Get the current day and do "case(day)" to utter the correct day's timetable.
        #print(datetime.today().weekday())


        # data = {
        #         "payload": 'cardsCarousel',
        #         "data": [
        #             {
        #                 #"image": "C:/Users/mibal/OneDrive/Desktop/RASAIll",
        #                 "title": "303COM",
        #                 "description": {
        #                                   "date": "Monday (04/04/22) ",
        #                                   "time": "3:00pm - 5:00pm",
        #                                   "title": "Individual Project",
        #                                     "lecturer": "Mr Peter Every",
        #                                    "room": "Online",
        #                                    "building": ""
        #                                 }
        #             }
        #         ]
        #     }

        # dispathcer.utter_message(json_message=data)        

        data = {
                "payload": 'cardsCarousel',
                "data": [
                    {
                        "title": "A320DEL",
                        "description": {
                                          "time":  "Friday 08.04.22",
                                          "date": "11:00am - 1:00pm",
                                          "title": "Absolut Beginner's German 3",
                                           "room": "Online",
                                           "lecturer": "Mrs Gabriele Siemon",
                                           "building": ""
                                           }
                    }, 
                ]
            }
        dispathcer.utter_message(text="Here is your timetable for today:",json_message=data)        
        #end = time.time()
        # print(f"The time it took is: {end-startTime}")

        return []


class ActionTimetableWeek(Action):
 
    def name(self) -> Text:
        return "action_ask_timetable_week"

    def run(self, dispathcer: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text ,Any]]:
        
        # startTime = time.time()

        # options = ChromeOptions()
        # options.headless = True
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # s = Service('C:/SeleniumDrivers/chromedriver')

        # driver = webdriver.Chrome(service=s, options=options)

        # driver.get("https://webapp.coventry.ac.uk/Timetable-main/Show/8246819?f=&t=&d=20220225&u=EEC/Timetable&k=Z4ZhqK$x4OdZtHHno$SZIOLrFa0.X#view=agendaWeek")
        # driver.implicitly_wait(30)

        # titles = []
        # details = []

        # #find the button that selects the week's calandar and clicks it
        # driver.find_element(by=By.XPATH, value='.//*[@id="calendar"]/table/tbody/tr/td[3]/span[4]').click()
        
        # #the parent element containing all the slots later to be clicked on to reveal the data rich pop-ups
        # parent_elem = driver.find_elements(by=By.XPATH, value=".//div[@class='fc-event fc-event-vert fc-event-start fc-event-end']")

        # #iterate over the div's considering the lenght of the parent element
        # for b in range(1, len(parent_elem)+1):
            
        #     try:
        #         #open the box
        #         div = driver.find_element(by=By.XPATH,value=f'//*[@id="calendar"]/div/div/div/div[3]/div/div/div[{b}]').click()

        #         #title div
        #         someDiv = driver.find_element(by=By.XPATH, value='./html/body/div[5]/div[1]')
        #         title = someDiv.text
        #         titleFin = title.replace('\n', '').replace('close','')

        #         #details div
        #         someOtherDiv = driver.find_element(by=By.XPATH, value='.//*[@id="popup"]')
        #         detail = someOtherDiv.text

        #         dispathcer.utter_message(text=f"{titleFin}{detail}")

        #         #close the box
        #         driver.find_element(by=By.XPATH, value='./html/body/div[5]/div[1]/a').click()

        #     except:
        #         break
               
        # driver.quit()

        # end = time.time()

        # print(end-startTime)

        data = {
                "payload": 'cardsCarousel',
                "data": [
                    {
                        "title": "303COM",
                        "description": {
                                          
                                          "date": "Monday 04.04.22 ",
                                          "time": "1:00pm - 2:00pm",
                                          "title": "Individual Project",
                                           "room": "online",
                                           "lecturer": "Mr Peter Every",
                                           "building": ""
                                           }
                    },                          
                    {
                        "title": "302CEM",
                        "description": {
                                          "date":  "Tuesday 05.04.22",
                                          "time": "3:00pm - 5:00pm",
                                          "title": "Agile Development Description",
                                           "room": "BSB213",
                                           "lecturer": "Mr Mark Tyers",
                                           "building": "Beatrice Shilling Building"
                                           }
                    },
                    {
                        "title": "380CT",
                        "description": {
                                          "date":  "Wendsday 06.04.22",
                                          "time": "09:00am - 11:00am",
                                          "title": "Theoretical Aspects of Computer Science",
                                           "lecturer": "Mr Kamal Bentahar",
                                           "room": "Online",
                                           "building": ""
                                           }
                    },
                    {
                        "title": "302CEM",
                        "description": {
                                          "time":  "Thursday 07.04.22",
                                          "date": "3:00pm - 5:00pm",
                                          "title": "Agile Development Description",
                                           "lecturer": "Mr Mark Tyers",
                                           "room": "BSB213",
                                           "building": "Beatrice Shilling Building"
                                           }
                    },
                    {
                        "title": "A320DEL",
                        "description": {
                                          "time":  "Friday 08.04.22",
                                          "date": "11:00am - 1:00pm",
                                          "title": "Absolut Beginner's German 3",
                                           "room": "Online",
                                           "lecturer": "Mrs Gabriele Siemon",
                                           "building": ""
                                           }
                    }, ]}

        dispathcer.utter_message(text="Here is your timetable for this week:",json_message=data)        

        return []


##### Video
class ActionGiveVideo(Action):

    def name(self) -> Text:
        return "action_ask_video_week_1"

    def run(self, dispathcer: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text ,Any]]:

        msg = { "type": "video", "payload": { "title": "Link name", "src": "https://www.youtube.com/embed/iyfJ0jx87w0" } }
        dispathcer.utter_message(text="Check this video",attachment=msg)

        return []


# ##### Dropdown
# class ActionGiveSchedule(Action):

#     def name(self) -> Text:
#         return "action_ask_supervisor_meeting_schedule"

#     def run(self, dispathcer: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text ,Any]]:

#         data=[ {"label":"Monday (12th April) ","value":"/inform{'121date':'12th April'}"},
#                {"label":"Wendsday (14th April) ","value":"/inform{'121date':'14th April'}"},
#                {"label":"Thursday (15th April)","value":"/inform{'121date':'15th April'}"} ]

#         message={"payload":"dropDown","data":data}
#         dispathcer.utter_message(text="Choose one of the available dates",json_message=message)

#         return []


##### Chart
class ActionGiveGrades(Action):

    def name(self) -> Text:
        return "action_ask_grades"

    def run(self, dispathcer: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text ,Any]]:

        data={  "title": "Grades", 

                "labels": [ "303COM (CW1)", "303COM (CW2)" , "302CEM (CW)", "380CT (Tst)", "380CT (CW)", "380CT (Ex)" , "A320DEL (Ex)" ],

                "backgroundColor": [ "#7fdb46", "#7fdb46", "#7fdb46", "#7fdb46", "#db4646", "#7fdb46", "#7fdb46" ], 

                "chartsData": [ 69, 83, 55, 69, 38, 76, 69], 

                "chartType": "bar", 

                "displayLegend": "true" }

        message={ "payload": "chart", "data": data }
        dispathcer.utter_message(text="Here are your grades",json_message=message)
        
        # data={ "title": "Leaves", "labels": [ "Sick Leave", "Casual Leave", "Earned Leave", "Flexi Leave" ], "backgroundColor": [ "#36a2eb", "#ffcd56", "#ff6384", "#009688", "#c45850" ], "chartsData": [ 5, 10, 22, 3 ], "chartType": "pie", "displayLegend": "true" }

        # message={ "payload": "chart", "data": data }

        # dispathcer.utter_message(text="Here are your leave balance details",json_message=message)

        return []


#### Collapsible
class ActionGiveModuleInfo(Action):

    def name(self) -> Text:
        return "action_ask_modules_info"

    def run(self, dispathcer: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text ,Any]]:

        data= [ { "title": "303COM", "description": """The final year project is the culmination of your degree programme. It allows you to work on a substantial problem in Computer Science, Computing, Ethical Hacking, Games Technology, Multimedia or Business Information Technology for an extended period of time. It allows you to demonstrate your competence as a computing professional, and to apply what you have learnt in the other components of your degree.
                                                    This module tests your ability to:
                                                    1.   Propose a suitable research question or practical computing related problem
                                                    2.   Carry out a substantial problem-solving task of your own choosing
                                                    3.   Work independently to prioritize the different components of your project, as well as balancing the project, as a whole, against other work;
                                                    4.   Take decisions, and to justify them convincingly.
                                                    It is your responsibility to lead your project, to attend your supervision meetings and to ask for the advice that you need. The project is an opportunity to demonstrate problem solving skills. It must include a substantial piece of primary research.
                                                    The project can be in any area of Computing including Artificial Intelligence, Robotics, Software Engineering, Business Process Improvement, Data Mining, Cloud Computing, Database theory, Computational Theory, Human-Computer Interaction, Usability, Mobile Development, Security, Web Application Development, game development or Multimedia. 
                                                    The project will NOT consist of only a literature review, nor will a secondary research summary be deemed sufficient to meet the learning outcomes. 
                                                    All projects must embed a significant piece of primary research and you will be asked to define a research question at the start of the project and develop a plan to evaluate your primary research to develop a solution. During the project you will need to evaluate alternative approaches and solutions to problems. It is important that you document these decisions as they should form a substantial part of your Project Report.
                                                    """ }, 
                { "title": "302CEM", "description": """Aims and Summary:
                                                    This module aims to provide students with sound understanding and experience in Development methodologies, techniques and tools. Agile and rapid approaches to developing information systems and software are critical for responding to changing business environments. The module will examine in detail different methodologies for rapid development and their application in practice. Specific industry strength types of technology for RAD will be utilised for solving real-world problems.
                                                    Learning Outcomes:
                                                    On completion of this module the student should be able to:
                                                    Demonstrate a sound understanding of how Agile Methodologies can be used to define users’ requirements, analysis and design of information systems.
                                                    Compare and contrast a range of current and emerging agile methodologies.
                                                    Evaluate the methods, techniques and tools for rapid development of various types of information systems, and the reasons for their selection and use.
                                                    Use a range of appropriate tools to contribute to the development of a solution to a real-world problem.
                                                    """ }, 
                { "title": "380CT", "description": """Module aim:
                                                    This module aims to give you a practical and theoretical understanding of the foundations of computer science.
                                                    It includes formal specification of patterns and languages. 
                                                    It describes different models of computation and the issues of computability and complexity. 
                                                    It also explores algorithmic techniques used to tackle complex problems.
                                                     Aims and Summary:
                                                    This module is designed to help you understand the theoretical foundations of Computer Science, and from this an appreciation of the limitations of computation and the important questions that remain open to this day.
                                                    The module covers: formal specification of languages; the main models m computation; and what these tell us about issues of computability and complexity.
                                                    Intended Module Learning Outcomes:
                                                    Upon completion of the module, you will have achieved the following:
                                                    Demonstrate the ability to use formal notation to specify patterns and languages.
                                                    Specify and be able to simulate various types of automata.
                                                    Demonstrate the ability to explain the connection between algorithms, models of computation, and language classes.
                                                    Classify the computability and complexity of problems.
                                                    """}, 
                { "title": "A320DEL", "description": """This is an AddVantage module for students with no previous knowledge of German. If you are NOT an absolute beginner, then you must register without delay for an alternative module at the AddVantage Scheme Reception located in The Hub.
                                                    Teaching and learning:
                                                    This module is run entirely ONLINE via Aula. There will be class every week for eleven weeks (including all assessment). Teaching and learning cover the four language skills of listening, speaking, reading and writing.  The module may run in either Semester 1 or 2.
                                                    You are expected to undertake any required preparation or practice exercises set by your tutor and actively participate in pair/group work, as directed.  It is essential to engage in regular independent study. 
                                                    See your online timetable for the timetabled sessions. 
                                                    On this module you should learn how to: 
                                                    1.   greet others (in)formally; give and understand basic information about yourself and others
                                                    2.   understand German numbers and the alphabet
                                                    3.   ask about and give basic study and work details
                                                    4.   state hobbies and interests
                                                    5.   express simple opinions
                                                    """ } ]

        message={ "payload": "collapsible", "data": data }
        dispathcer.utter_message(text="Here are all your modules for this semester: ",json_message=message)

        return []


#### Collapsible
class ActionGiveTeacherInfo(Action):

    def name(self) -> Text:
        return "action_ask_teacher_info"

    def run(self, dispathcer: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text ,Any]]:

        data= [ { "title": "Mr Peter Every", "description": "email@coventry.com" },
                { "title": "Mr Mark Tyers", "description": "email@coventry.com" }, 
                { "title": "Mr Kamal Bentahar", "description": "email@coventry.com" }, 
                { "title": "Mrs Gabriele Siemon", "description": "email@coventry.com" } ]

        message={ "payload": "collapsible", "data": data }
        dispathcer.utter_message(text="Here are your lecturer's contact details",json_message=message)

        return []


#### Collapsible
class ActionGiveAssesmentInfo(Action):

    def name(self) -> Text:
        return "action_ask_assesment_info"

    def run(self, dispathcer: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text ,Any]]:


        data= [ { "title": "303COM - Individual Project (30cr) ", 
                "description": "Coursework: 19/04/2022 " }, 
                
                { "title": "302CEM - Agile Development (20cr) ", 
                "description": "Courswork: 12/04/2022 " }, 

                { "title": "380CT - Theoretical Aspects of Computer Science (20cr) ", 
                "description": "Phase test: 10/03/2022  Coursework: 6/04/2022  Exam: 11/04/2022 " }, 

                { "title": "A320DEL - Absolut Beginner's German 3 ", 
                "description": "Exam: 09/04/2022" } ]

        message={ "payload": "collapsible", "data": data }
        dispathcer.utter_message(text="Assignments",json_message=message)

        return []


### Text - Time 
class ActionGiveAssesmentInfo(Action):
    def name(self) -> Text:
        return "action_give_current_time"

    def run(self, dispathcer: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text ,Any]]:

        time = time.now()
        print(time)

        dispathcer.utter_message(text=f"{time}")

        return []


### Text - Jokes 
class ActionGiveJoke(Action):
    def name(self) -> Text:
        return "action_give_joke"

    def run(self, dispathcer: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text ,Any]]:
        
        joke = pyjokes.get_joke()
        dispathcer.utter_message(text=joke)
        
        return []




