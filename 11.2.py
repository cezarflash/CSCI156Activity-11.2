__author__ = 'Ayla'
#1. Create a dictionary called transcript that has keys for the semesters that you have been at AU. Set the corresponding values to a list of
#lists of the courses taken during that semester. Each course is a list:
#[Four digit subject, Course Number, Section, Title].
#For Fall14 [CSCI,156,01,'Computer Science I'] would be one of the courses in your list. Don't worry about the accuracy of
#the section data, no one is going to compare your transcript with your program. Make up at least two years worth of data.

transcript={'Fall 2011':[['CHEM',105,1,"General Chemistry I"],['CHEM,105L',105,2,'Laboratory General Chem I'],
                         ['ENGL',101,1,'Writing I'],['EQUS',103,1,'English Riding III'],['SPAN',101,1,'FYE Spanish I']],
            'Spring 2012':[['BIOL',202,1,'Biology II'],['CHEM',106,1,'General Chemistry II'],['CHEM',106,2,'Laboratory General Chem II'],
                           ['ENGL',102,1,'Writing II'],['EQUS',111,1,'Western Riding: Level II']],
            'Fall 2012':[['BIOL',201,1,'Biology I'],['HIST',120,1,'The Ancient Mediterranean'],['MATH',151,1,'Calculus I'],
                         ['PSYC',101,1,'Introduction to Psychology']],
            'Spring 2013':[['ENGL',281,1,'Literature and Science'],['EQUS',200,1,'Topics in Equine Vet Medicine'],
                           ['MUSC',200,1,'Topics:Reel Music in America'],['PSYC',282,1,'Social Psychology'],
                           ['SPAN',102,1,'Introductory Spanish II']],
            'Fall 2013':[['PSYC',118,1,'Intro Adult Development/Aging'],['PSYC',220,1,'Pych Methods and Statistics'],
                         ['PSYC',210,1,'Communication/Counseling'],['PSYC',330,1,'Neuropsychology'],
                         ['PSYC',341,1,'Theories of Personality']],
            'Spring 2014':[['PYSC',230,1,'Psch Research and Design'],['PSYC',322,1,'Health Psychology'],
                           ['PSYC',332,1,'Cognitive Processes'],
                           ['PSYC',342,1,'Abnormal Psych'],['RLGS',105,1,'Intro to World Religions']],
            'Fall 2014':[['ANTH',110,1,'Cultural Anthropology'],['CSI',156,1,'Computer Science'],
                         ['EQUS',105,1,'Introduction to Dressage'],['EQUS',200,1,'Topics: Basic Horsemanship and Groundwork'],
                         ['PSYC',491,1,'Clinical Procedures'],['PSYC',497,1,'Senior Seminar']]}




#2. Write a procedure that prints your transcript in a nice way.

def printtranscript(transcript):
    for semesters in transcript:
        print(semesters)
        for classes in transcript[semesters]:
            print(' ' +classes[0]+' '+ str(classes[1])+' '+str(classes[2])+' '+classes[3])




printtranscript(transcript)

#3. Write a procedure semesters(subject) which returns a list of the semesters in which you took a course in the subject
#area subject. So if called subject('MATH') then you would get back a list of the semesters in which you took a math class.

def semesters(subject,transcript):
    for semester in transcript:
         for course in transcript[semester]:
             if course[0] == subject:
                    print(semester)
                    break


semesters('PSYC',transcript)

