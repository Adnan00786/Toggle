import datetime

def time_table_generator():
    def get_check(CLASS,EXAM,STREaM,cid):
        CLASS = int(CLASS)
        from datetime import date
            
        # Set the exam date
        exam_year = 2023
        exam_month = 2
        exam_day = 15
        exam_date = date(exam_year, exam_month, exam_day)
        current_time = datetime.datetime.now()
        # Calculate the number of days left until the exam
        current_date = date.today()
        days_left = exam_date - current_date
        productive_hours = 8
        no_days_left = days_left.days
        hours_left = productive_hours*no_days_left
        print("hours left",hours_left)
        if CLASS == 12 and EXAM == "CBSE" and STREaM == "s":#science
            n_chem_syllabus = 10 
            n_phy_syllabus = 14
            n__math_syllabus = 13
            n_CS_syllabus = 9
            n_english_syllabus = 19
            ### chapter coverage ###
            # Chemistry Time per chapter per day 
            n_hour_per_chapter_chem_theory = 1
            n_hour_per_chapter_chem_practice = 2
            per_day_chem = n_hour_per_chapter_chem_practice + n_hour_per_chapter_chem_theory
            # Physics Time per chapter per day 
            n_hour_per_chapter_phy_revise = 1
            n_hour_per_chapter_phy_practice = 2
            per_day_phy = n_hour_per_chapter_phy_practice + n_hour_per_chapter_phy_revise
            # English Time per chapter per day 
            n_hour_per_chapter_eng_chapter_summanry = 1
            n_hour_per_chapter_eng_practice = 2
            per_day_eng = n_hour_per_chapter_eng_chapter_summanry + n_hour_per_chapter_eng_practice

            # CS Time per chapter per day 
            n_hour_per_chapter_CS_chapter_summary = 1
            n_hour_per_chapter_CS_practice = 2
            per_day_CS = n_hour_per_chapter_CS_chapter_summary + n_hour_per_chapter_CS_practice

            # Math Time per chapter per day 
            n_hour_per_chapter_Maths_formula_revision = 0.5
            n_hour_per_chapter_Maths_practice = 2.5
            per_day_math = n_hour_per_chapter_Maths_practice + n_hour_per_chapter_Maths_formula_revision
            # Total time required 
            total_time_required = int(((n_chem_syllabus)*(per_day_chem)) +((n__math_syllabus)*(per_day_math)) +((n_phy_syllabus)*(per_day_phy)) +((n_CS_syllabus)*(per_day_CS)) +((n_english_syllabus)*(per_day_eng)) )
            print(total_time_required)
            # per day coverage 
            subjects_coverage = [per_day_chem,per_day_CS,per_day_eng,per_day_math,per_day_phy]
            SUBJECTS = ['PHYSICS','CHEMISTRY','MATHEMATICS','ENGLISH','COMPUTER SCIENCE']
            # for subjects in SUBJECTS:
                # print(subjects)
            per_day_study_compulsory = ['MATHEMATICS','PHYSICS'] # MATH and PHYSICS complete time and CS 1 hr and english 1 hr and next day chemistry 2 hr 
            per_study_left = ["CHEMISTRY","ENGLISH","COMPUTER SCIENCE"]
            file_c_id = "plan of customer with ID {}.txt".format(cid)
            with open(file_c_id,'a') as plan_intro_maker:
                plan_intro_maker.write("Study According to this plan\n\nMaths formula revision = 0.5hr and Math Practice = 2.5hr\nPhysics theory and formula revision for 1 hr and 2hr practice \nEnglish and Computer Science revise theory for 1 hr and practice 2hr\n\n")
            count = 1
            print("days left",days_left.days)
            for i in range(days_left.days):    
                # global count
                for a,b in zip(per_day_study_compulsory,per_study_left):
                    if count>days_left.days:
                        break
                    data_print = "Day{}\nSubject 1: {}\nSubject 2: {}\nTake breaks of 30 mins after every 3 hours\n\n".format(count,a,b)
                    with open(file_c_id,'a') as plan_maker:
                        plan_maker.write(data_print)
                        # print(type(data_print))
                    count += 1
            print(count)


    get_check(12,"CBSE",'s',1)

time_table_generator()