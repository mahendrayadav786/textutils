from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request, "index.html")

def analyse(request):

      #POST THE TEXT
      djtext = request.POST.get("text", "default")
      print(djtext)

      #---------Remove Punctuation----------------#
      checkbox = request.POST.get("removepunc", "off")
      print(checkbox)

      #-------------capitalized first letter---------------------##
      capfirst = request.POST.get("capfirst", "off")

      #--------------REMOVE  LINE-----------#
      new_line_remover = request.POST.get("removeline", "off")

      #-------------------extra_space_remover------------------#######
      extra_space_remover = request.POST.get("extra_space_remover", "off")

       #----------------Too check capitalize is on ---------------#
      capitalized = request.POST.get("capitalized", "off")


      punctuation =' ' '  !@#$%^&*(){}' '|"\/.,~"   ' ' '

      #-------CAHECK PUNCTUATION BOX IS ON--------#########

      if checkbox =="on":
            analysed_text = ""
            for char  in djtext:
                  if char not in punctuation:
                        analysed_text = analysed_text+char

            params = {"purpose": "Analysed text","analysed": analysed_text}

            djtext = analysed_text

      if capfirst == "on":
            analysed_text= ""
            analysed_text = analysed_text+djtext.capitalize()
            params = {"purpose": "Capitalized ", "analysed": analysed_text}
            djtext  = analysed_text

      ############New line remover##############
      if new_line_remover == "on":
             analysed_text =""
             for char in djtext:
                  if char != "\n" and char != "\r":
                        analysed_text = analysed_text + char

             params = {"purpose": "New line remover", "analysed": analysed_text}
             djtext = analysed_text

      ##########----------------Extra space remover-------------------#########

      if (extra_space_remover == "on"):
          analyzed_text = ""
          for index, char in enumerate(djtext):
              if not (djtext[index] == " " and djtext[index + 1] == " "):
                  analyzed_text = analyzed_text + char

          params = {'purpose': 'Removed NewLines', 'analysed': analyzed_text}

          # Analyze the text
          djtext = analysed_text

      #----------Capitalized Letter------------------#
      if capitalized == "on":
            analysed_text =""
            analysed_text=  djtext.upper()
            params = {"purpose": "Capitalized ", "analysed": analysed_text}
            djtext = analysed_text

      return render(request, "analyse.html", params)







