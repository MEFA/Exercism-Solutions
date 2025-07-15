"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    new_student_scores = []
    for score in student_scores: 
        new_score = round(score)
        new_student_scores.append(new_score)
    return new_student_scores

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    total_number = 0
    for score in student_scores:
        if score <= 40:
            total_number += 1
    return total_number

def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    above_threshold_list= []
    for score in student_scores:
        if score >= threshold:
            above_threshold_list.append(score) 
    return above_threshold_list

def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    threshold_denominator = (highest-40)/4
    final_list=[41]
    for each_iteration in final_list:
        next_upper_threshold = each_iteration + threshold_denominator
        if next_upper_threshold >= highest:
            break
        final_list.append(round(next_upper_threshold))
        
    return final_list


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    rank = 0
    rank_list = []
    for score in student_scores:
        rank += 1
        rank_list.append(rank)
    
    result = [str(item1)+". "+str(item2) +": " + str(item3) for item1, item2, item3 in zip(rank_list,student_names,student_scores)]

    return result


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for student in student_info:
        if student[1]==100:
            return student

    return []
