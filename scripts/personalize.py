from core.models import SurveyAnswerItem, Answer ,AnswerGoal, AnswerExclusion, ResultItem, AnswerItem, Question
from orders.models import Order, OrderResultItem, SurveyResult, SurveyResultItem, ItemOrder


def GetOrderStatus():
    #getting all order with paymant accepted status
    #for this order create Survey Answers

    print('get order paument succesful')
    order_payment_succesful = Order.objects.filter(order_status = "PA").all()
    for o in order_payment_succesful:
        
        
        survey = ItemOrder.objects.filter(order = o).last().survey
        print('survey: ', str(survey))


        Personalize(survey=survey, order=o)
        






def Personalize(survey, order):
    #get answers for survey
    answers = SurveyAnswerItem.objects.filter(survey=survey).all()

    #get 
    survey_result = SurveyResult.objects.filter(survey=survey).last()

    survey_ans =[]
    

    #for answer add goal
    for a in answers:
        #get type question
        print('a: ', str(a.answer.answer))
        
        ans = AnswerItem.objects.filter(answer=a.answer).last()
        que = Question.objects.filter(name=ans).last()
        print('ans: ', str(ans))
        print('que: ', str(que.question_type))
       

        #don't touch    
        result_item = AnswerGoal.objects.filter(answer=a.answer)
        
        for r in result_item:
            survey_ans.append(r.result_item.slug)
            

    #clear duplicate in survey result answers
    survey_ans = list(dict.fromkeys(survey_ans))



    answers = SurveyAnswerItem.objects.filter(survey=survey).all()
    
    #for answer remove exclusions 
    for a in answers:
        result_item = AnswerExclusion.objects.filter(answer=a.answer)

        for r in result_item:

            if r.result_item.slug != None:
                #pass
                try: 
                    survey_ans.remove(r.result_item.slug)
                except:
                    pass
            
    
    print('survey result: ', str(survey_ans))
    #add to Survey Result
    
    for s in survey_ans:
        #print('s: ', str(s))
        result_item = ResultItem.objects.filter(slug=s).last()
        survey_answer_result = SurveyResultItem.objects.create(survey=survey_result, result_item=result_item)
        #print('s_a: ', str(survey_answer_result.survey), ' ', str(survey_answer_result.result_item))
    print('for survey ',str(survey), ' created Survey Answers Result Items')

    CreateOrderResult(survey=survey, order=order)
    
    
    #TODO: add to result item
        

def CreateOrderResult(survey, order):
    #TODO: create Order Result




    #change order status to Waiting For Acceept
    order = Order.objects.filter(order_id = order)
    order.update(order_status="WA")
    