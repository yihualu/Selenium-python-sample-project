#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Nov 27, 2017

@author: edward
'''
from selenium import webdriver
import urlparse
import logging
import os 
import unittest

#Properties
browserToTest = "Chrome"   #supported browsers:Chrome
chromeDriverPath = os.path.join(os.path.dirname(os.path.realpath(__file__)),"chromedriver")

applicationPath = os.path.join(os.path.dirname(os.path.realpath(__file__)),"FusionSportQA_testproject.html")
applicationURL = urlparse.urljoin('file:', applicationPath)

#web element ids
inputTextAreaID = "txtInput"
outputTextAreaID = "txtOutput"
reverseTextBtnID = "flip1"
reverseWordingBtnID = "flip2"
flipSentenceBtnID = "flip3"

#test data
inputList = [     "",    #empty string
                  " ",  #string with only one space
                  "string   with  multiple  spaces   between  words",
                  " string with one space at the beginning",
                  "   string with multiple spaces at the beginning",
                  "string with one space at the end ",
                  "string with multiple spaces at the end   ",
                  " string with one space at beginning and end ",
                  "   string with multiple spaces at beginning and end    ",
                  "string with alphanumeric abced1234",
                  "string with alphanumeric and special characters abced1234&^* 321(*^kkd",
                  "string which are palindrome emordnilap era hcihw gnirts",
                  "a", #string with only one character
                  "string with 100 characterstring with 100 characterstring with 100 characterstring with 100 character",
                  "STRING WITH lower case and UPPER CASE letters",
                  "!@#$%^&*() (*&^%$$%&&", #string with only special characters
                  u"这是一句中文， 这是第二句", #string with Chinese characters
                  ]


expectedReverseTextOutputList = [   ""
                                    ," "                  
                                    ,"sdrow  neewteb   secaps  elpitlum  htiw   gnirts"                  
                                    ,"gninnigeb eht ta ecaps eno htiw gnirts "                  
                                    ,"gninnigeb eht ta secaps elpitlum htiw gnirts   "                  
                                    ," dne eht ta ecaps eno htiw gnirts"                  
                                    ,"   dne eht ta secaps elpitlum htiw gnirts"                  
                                    ," dne dna gninnigeb ta ecaps eno htiw gnirts "                  
                                    ,"    dne dna gninnigeb ta secaps elpitlum htiw gnirts   "                  
                                    ,"4321decba ciremunahpla htiw gnirts"                  
                                    ,"dkk^*(123 *^&4321decba sretcarahc laiceps dna ciremunahpla htiw gnirts"                  
                                    ,"string which are palindrome emordnilap era hcihw gnirts"                  
                                    ,"a"                  
                                    ,"retcarahc 001 htiw gnirtsretcarahc 001 htiw gnirtsretcarahc 001 htiw gnirtsretcarahc 001 htiw gnirts"                  
                                    ,"srettel ESAC REPPU dna esac rewol HTIW GNIRTS"                  
                                    ,"&&%$$%^&*( )(*&^%$#@!"                  
                                    ,u"句二第是这 ，文中句一是这"                  
                                 ]

expectedReverseWordingOutputList = [""
                                    ," "                  
                                    ,"words  between   spaces  multiple  with   string"                  
                                    ,"beginning the at space one with string "                  
                                    ,"beginning the at spaces multiple with string   "                  
                                    ," end the at space one with string"                  
                                    ,"   end the at spaces multiple with string"                  
                                    ," end and beginning at space one with string "                  
                                    ,"    end and beginning at spaces multiple with string   "                  
                                    ,"abced1234 alphanumeric with string"                  
                                    ,"kkd^*(321 *^&abced1234 characters special and alphanumeric with string"                  
                                    ,"gnirts hcihw era emordnilap palindrome are which string"                  
                                    ,"a"                  
                                    ,"character 100 with characterstring 100 with characterstring 100 with characterstring 100 with string"                  
                                    ,"letters CASE UPPER and case lower WITH STRING"                  
                                    ,"&&%$$%^&*( )(*&^%$#@!"                  
                                    ,u"句二第是这 ，文中句一是这" 
                      ]

expectedFlipOneSentenceOutputList = expectedReverseWordingOutputList

#global variables
driver = None

def getDriver():
    global driver
    if driver == None:
        if browserToTest == "Chrome":
            driver = webdriver.Chrome(chromeDriverPath)
        else:
            logging.error("please specified a supported browser")
    return driver

class ReversePage(object):
    def __init__(self):
        driver = getDriver()
        driver.implicitly_wait(30)
        driver.maximize_window()
        # navigate to the application home page
        driver.get(applicationURL)
    
    def getInputText(self):
        return driver.find_element_by_id(inputTextAreaID).get_attribute("value")    
    def setInputText(self,inputText):
        inputElement = driver.find_element_by_id(inputTextAreaID)
        inputElement.clear()
        inputElement.send_keys(inputText)
        
    def getOutputText(self):
        return driver.find_element_by_id(outputTextAreaID).get_attribute("value")
    def setOutputText(self,outputText):
        outputElement = driver.find_element_by_id(outputTextAreaID)
        outputElement.clear()
        outputElement.send_keys(outputText)
    
    def clickReverseTextBtn(self):
        driver.find_element_by_id(reverseTextBtnID).click()
    def clickReverseWordingBtn(self):
        driver.find_element_by_id(reverseWordingBtnID).click()
    def clickFlipSentenceBtn(self):
        driver.find_element_by_id(flipSentenceBtnID).click()

    

class TestReverse(unittest.TestCase):
    reversePage = ReversePage()
        
    def setUp(self):
        getDriver().get(applicationURL)
    
    def test_reverseTextCase1(self):
        self.reversePage.setInputText(inputList[0])
        self.reversePage.clickReverseTextBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseTextOutputList[0], actualResult, "Reverse Text of empty string" + ", Expected:" + expectedReverseTextOutputList[0] + ", Actual:" + actualResult )   
    
    def test_reverseTextCase2(self):
        self.reversePage.setInputText(inputList[1])
        self.reversePage.clickReverseTextBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseTextOutputList[1], actualResult, "Reverse Text of string with only one space" + ", Expected:" + expectedReverseTextOutputList[1] + ", Actual:" + actualResult)   

    def test_reverseTextCase3(self):
        self.reversePage.setInputText(inputList[2])
        self.reversePage.clickReverseTextBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseTextOutputList[2], actualResult, "Reverse Text of string   with  multiple  spaces   between  words" + ", Expected:" + expectedReverseTextOutputList[2] + ", Actual:" + actualResult)
    
    def test_reverseTextcase4(self):
        self.reversePage.setInputText(inputList[3])
        self.reversePage.clickReverseTextBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseTextOutputList[3], actualResult, "Reverse Text of string with one space at the beginning"+ ", Expected:" + expectedReverseTextOutputList[3] + ", Actual:" + actualResult)

    def test_reverseTextcase5(self):
        self.reversePage.setInputText(inputList[4])
        self.reversePage.clickReverseTextBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseTextOutputList[4], actualResult, "Reverse Text of    string with multiple spaces at the beginning"+ ", Expected:" + expectedReverseTextOutputList[4] + ", Actual:" + actualResult)
    
    def test_reverseTextcase6(self):
        self.reversePage.setInputText(inputList[5])
        self.reversePage.clickReverseTextBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseTextOutputList[5], actualResult, "Reverse Text of string with one space at the end "+ ", Expected:" + expectedReverseTextOutputList[5] + ", Actual:" + actualResult)

    def test_reverseTextcase7(self):
        self.reversePage.setInputText(inputList[6])
        self.reversePage.clickReverseTextBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseTextOutputList[6], actualResult, "Reverse Text of string with multiple spaces at the end   "+ ", Expected:" + expectedReverseTextOutputList[6] + ", Actual:" + actualResult)

    def test_reverseTextcase8(self):
        self.reversePage.setInputText(inputList[7])
        self.reversePage.clickReverseTextBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseTextOutputList[7], actualResult, "Reverse Text of  string with one space at beginning and end "+ ", Expected:" + expectedReverseTextOutputList[7] + ", Actual:" + actualResult)

    def test_reverseTextcase9(self):
        self.reversePage.setInputText(inputList[8])
        self.reversePage.clickReverseTextBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseTextOutputList[8], actualResult, "Reverse Text of    string with multiple spaces at beginning and end    "+ ", Expected:" + expectedReverseTextOutputList[8] + ", Actual:" + actualResult)

    def test_reverseTextcase10(self):
        self.reversePage.setInputText(inputList[9])
        self.reversePage.clickReverseTextBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseTextOutputList[9], actualResult, "Reverse Text of string with alphanumeric"+ ", Expected:" + expectedReverseTextOutputList[9] + ", Actual:" + actualResult)

    def test_reverseTextcase11(self):
        self.reversePage.setInputText(inputList[10])
        self.reversePage.clickReverseTextBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseTextOutputList[10], actualResult, "Reverse Text of string with alphanumeric and special characters"+ ", Expected:" + expectedReverseTextOutputList[10] + ", Actual:" + actualResult)

    def test_reverseTextcase12(self):
        self.reversePage.setInputText(inputList[11])
        self.reversePage.clickReverseTextBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseTextOutputList[11], actualResult, "Reverse Text of string which are palindrome"+ ", Expected:" + expectedReverseTextOutputList[11] + ", Actual:" + actualResult)

    def test_reverseTextcase13(self):
        self.reversePage.setInputText(inputList[12])
        self.reversePage.clickReverseTextBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseTextOutputList[12], actualResult, "Reverse Text of string with only one character"+ ", Expected:" + expectedReverseTextOutputList[12] + ", Actual:" + actualResult)

    def test_reverseTextcase14(self):
        self.reversePage.setInputText(inputList[13])
        self.reversePage.clickReverseTextBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseTextOutputList[13], actualResult, "Reverse Text of string with 100 characters"+ ", Expected:" + expectedReverseTextOutputList[13] + ", Actual:" + actualResult)

    def test_reverseTextcase15(self):
        self.reversePage.setInputText(inputList[14])
        self.reversePage.clickReverseTextBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseTextOutputList[14], actualResult, "Reverse Text of STRING WITH lower case and UPPER CASE letters"+ ", Expected:" + expectedReverseTextOutputList[14] + ", Actual:" + actualResult)

    def test_reverseTextcase16(self):
        self.reversePage.setInputText(inputList[15])
        self.reversePage.clickReverseTextBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseTextOutputList[15], actualResult, "Reverse Text of string with only special characters"+ ", Expected:" + expectedReverseTextOutputList[15] + ", Actual:" + actualResult)

    def test_reverseTextcase17(self):
        self.reversePage.setInputText(inputList[16])
        self.reversePage.clickReverseTextBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseTextOutputList[16], actualResult, "Reverse Text of string with Chinese characters"+ ", Expected:" + expectedReverseTextOutputList[16] + ", Actual:" + actualResult)
     
    
    
    def test_reverseWordingCase1(self):
        self.reversePage.setInputText(inputList[0])
        self.reversePage.clickReverseWordingBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseWordingOutputList[0], actualResult, "Reverse wording of empty string" + ", Expected:" + expectedReverseWordingOutputList[0] + ", Actual:" + actualResult )   
    
    def test_reverseWordingCase2(self):
        self.reversePage.setInputText(inputList[1])
        self.reversePage.clickReverseWordingBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseWordingOutputList[1], actualResult, "Reverse wording of string with only one space" + ", Expected:" + expectedReverseWordingOutputList[1] + ", Actual:" + actualResult)   

    def test_reverseWordingCase3(self):
        self.reversePage.setInputText(inputList[2])
        self.reversePage.clickReverseWordingBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseWordingOutputList[2], actualResult, "Reverse wording of string   with  multiple  spaces   between  words" + ", Expected:" + expectedReverseWordingOutputList[2] + ", Actual:" + actualResult)
    
    def test_reverseWordingcase4(self):
        self.reversePage.setInputText(inputList[3])
        self.reversePage.clickReverseWordingBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseWordingOutputList[3], actualResult, "Reverse wording of string with one space at the beginning"+ ", Expected:" + expectedReverseWordingOutputList[3] + ", Actual:" + actualResult)

    def test_reverseWordingcase5(self):
        self.reversePage.setInputText(inputList[4])
        self.reversePage.clickReverseWordingBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseWordingOutputList[4], actualResult, "Reverse wording of    string with multiple spaces at the beginning"+ ", Expected:" + expectedReverseWordingOutputList[4] + ", Actual:" + actualResult)
    
    def test_reverseWordingcase6(self):
        self.reversePage.setInputText(inputList[5])
        self.reversePage.clickReverseWordingBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseWordingOutputList[5], actualResult, "Reverse wording of string with one space at the end "+ ", Expected:" + expectedReverseWordingOutputList[5] + ", Actual:" + actualResult)

    def test_reverseWordingcase7(self):
        self.reversePage.setInputText(inputList[6])
        self.reversePage.clickReverseWordingBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseWordingOutputList[6], actualResult, "Reverse wording of string with multiple spaces at the end   "+ ", Expected:" + expectedReverseWordingOutputList[6] + ", Actual:" + actualResult)

    def test_reverseWordingcase8(self):
        self.reversePage.setInputText(inputList[7])
        self.reversePage.clickReverseWordingBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseWordingOutputList[7], actualResult, "Reverse wording of  string with one space at beginning and end "+ ", Expected:" + expectedReverseWordingOutputList[7] + ", Actual:" + actualResult)

    def test_reverseWordingcase9(self):
        self.reversePage.setInputText(inputList[8])
        self.reversePage.clickReverseWordingBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseWordingOutputList[8], actualResult, "Reverse wording of    string with multiple spaces at beginning and end    "+ ", Expected:" + expectedReverseWordingOutputList[8] + ", Actual:" + actualResult)

    def test_reverseWordingcase10(self):
        self.reversePage.setInputText(inputList[9])
        self.reversePage.clickReverseWordingBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseWordingOutputList[9], actualResult, "Reverse wording of string with alphanumeric"+ ", Expected:" + expectedReverseWordingOutputList[9] + ", Actual:" + actualResult)

    def test_reverseWordingcase11(self):
        self.reversePage.setInputText(inputList[10])
        self.reversePage.clickReverseWordingBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseWordingOutputList[10], actualResult, "Reverse wording of string with alphanumeric and special characters"+ ", Expected:" + expectedReverseWordingOutputList[10] + ", Actual:" + actualResult)

    def test_reverseWordingcase12(self):
        self.reversePage.setInputText(inputList[11])
        self.reversePage.clickReverseWordingBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseWordingOutputList[11], actualResult, "Reverse wording of string which are palindrome"+ ", Expected:" + expectedReverseWordingOutputList[11] + ", Actual:" + actualResult)

    def test_reverseWordingcase13(self):
        self.reversePage.setInputText(inputList[12])
        self.reversePage.clickReverseWordingBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseWordingOutputList[12], actualResult, "Reverse wording of string with only one character"+ ", Expected:" + expectedReverseWordingOutputList[12] + ", Actual:" + actualResult)

    def test_reverseWordingcase14(self):
        self.reversePage.setInputText(inputList[13])
        self.reversePage.clickReverseWordingBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseWordingOutputList[13], actualResult, "Reverse wording of string with 100 characters"+ ", Expected:" + expectedReverseWordingOutputList[13] + ", Actual:" + actualResult)

    def test_reverseWordingcase15(self):
        self.reversePage.setInputText(inputList[14])
        self.reversePage.clickReverseWordingBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseWordingOutputList[14], actualResult, "Reverse wording of STRING WITH lower case and UPPER CASE letters"+ ", Expected:" + expectedReverseWordingOutputList[14] + ", Actual:" + actualResult)

    def test_reverseWordingcase16(self):
        self.reversePage.setInputText(inputList[15])
        self.reversePage.clickReverseWordingBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseWordingOutputList[15], actualResult, "Reverse wording of string with only special characters"+ ", Expected:" + expectedReverseWordingOutputList[15] + ", Actual:" + actualResult)

    def test_reverseWordingcase17(self):
        self.reversePage.setInputText(inputList[16])
        self.reversePage.clickReverseWordingBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedReverseWordingOutputList[16], actualResult, "Reverse wording of string with Chinese characters"+ ", Expected:" + expectedReverseWordingOutputList[16] + ", Actual:" + actualResult)
    
    def test_flipOneSentenceCase1(self):
        self.reversePage.setInputText(inputList[0])
        self.reversePage.clickFlipSentenceBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedFlipOneSentenceOutputList[0], actualResult, "Flip one sentence of empty string" + ", Expected:" + expectedFlipOneSentenceOutputList[0] + ", Actual:" + actualResult )   
    
    def test_flipOneSentenceCase2(self):
        self.reversePage.setInputText(inputList[1])
        self.reversePage.clickFlipSentenceBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedFlipOneSentenceOutputList[1], actualResult, "Flip one sentence of string with only one space" + ", Expected:" + expectedFlipOneSentenceOutputList[1] + ", Actual:" + actualResult)   

    def test_flipOneSentenceCase3(self):
        self.reversePage.setInputText(inputList[2])
        self.reversePage.clickFlipSentenceBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedFlipOneSentenceOutputList[2], actualResult, "Flip one sentence of string   with  multiple  spaces   between  words" + ", Expected:" + expectedFlipOneSentenceOutputList[2] + ", Actual:" + actualResult)
    
    def test_flipOneSentencecase4(self):
        self.reversePage.setInputText(inputList[3])
        self.reversePage.clickFlipSentenceBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedFlipOneSentenceOutputList[3], actualResult, "Flip one sentence of string with one space at the beginning"+ ", Expected:" + expectedFlipOneSentenceOutputList[3] + ", Actual:" + actualResult)

    def test_flipOneSentencecase5(self):
        self.reversePage.setInputText(inputList[4])
        self.reversePage.clickFlipSentenceBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedFlipOneSentenceOutputList[4], actualResult, "Flip one sentence of    string with multiple spaces at the beginning"+ ", Expected:" + expectedFlipOneSentenceOutputList[4] + ", Actual:" + actualResult)
    
    def test_flipOneSentencecase6(self):
        self.reversePage.setInputText(inputList[5])
        self.reversePage.clickFlipSentenceBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedFlipOneSentenceOutputList[5], actualResult, "Flip one sentence of string with one space at the end "+ ", Expected:" + expectedFlipOneSentenceOutputList[5] + ", Actual:" + actualResult)

    def test_flipOneSentencecase7(self):
        self.reversePage.setInputText(inputList[6])
        self.reversePage.clickFlipSentenceBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedFlipOneSentenceOutputList[6], actualResult, "Flip one sentence of string with multiple spaces at the end   "+ ", Expected:" + expectedFlipOneSentenceOutputList[6] + ", Actual:" + actualResult)

    def test_flipOneSentencecase8(self):
        self.reversePage.setInputText(inputList[7])
        self.reversePage.clickFlipSentenceBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedFlipOneSentenceOutputList[7], actualResult, "Flip one sentence of  string with one space at beginning and end "+ ", Expected:" + expectedFlipOneSentenceOutputList[7] + ", Actual:" + actualResult)

    def test_flipOneSentencecase9(self):
        self.reversePage.setInputText(inputList[8])
        self.reversePage.clickFlipSentenceBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedFlipOneSentenceOutputList[8], actualResult, "Flip one sentence of    string with multiple spaces at beginning and end    "+ ", Expected:" + expectedFlipOneSentenceOutputList[8] + ", Actual:" + actualResult)

    def test_flipOneSentencecase10(self):
        self.reversePage.setInputText(inputList[9])
        self.reversePage.clickFlipSentenceBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedFlipOneSentenceOutputList[9], actualResult, "Flip one sentence of string with alphanumeric"+ ", Expected:" + expectedFlipOneSentenceOutputList[9] + ", Actual:" + actualResult)

    def test_flipOneSentencecase11(self):
        self.reversePage.setInputText(inputList[10])
        self.reversePage.clickFlipSentenceBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedFlipOneSentenceOutputList[10], actualResult, "Flip one sentence of string with alphanumeric and special characters"+ ", Expected:" + expectedFlipOneSentenceOutputList[10] + ", Actual:" + actualResult)

    def test_flipOneSentencecase12(self):
        self.reversePage.setInputText(inputList[11])
        self.reversePage.clickFlipSentenceBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedFlipOneSentenceOutputList[11], actualResult, "Flip one sentence of string which are palindrome"+ ", Expected:" + expectedFlipOneSentenceOutputList[11] + ", Actual:" + actualResult)

    def test_flipOneSentencecase13(self):
        self.reversePage.setInputText(inputList[12])
        self.reversePage.clickFlipSentenceBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedFlipOneSentenceOutputList[12], actualResult, "Flip one sentence of string with only one character"+ ", Expected:" + expectedFlipOneSentenceOutputList[12] + ", Actual:" + actualResult)

    def test_flipOneSentencecase14(self):
        self.reversePage.setInputText(inputList[13])
        self.reversePage.clickFlipSentenceBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedFlipOneSentenceOutputList[13], actualResult, "Flip one sentence of string with 100 characters"+ ", Expected:" + expectedFlipOneSentenceOutputList[13] + ", Actual:" + actualResult)

    def test_flipOneSentencecase15(self):
        self.reversePage.setInputText(inputList[14])
        self.reversePage.clickFlipSentenceBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedFlipOneSentenceOutputList[14], actualResult, "Flip one sentence of STRING WITH lower case and UPPER CASE letters"+ ", Expected:" + expectedFlipOneSentenceOutputList[14] + ", Actual:" + actualResult)

    def test_flipOneSentencecase16(self):
        self.reversePage.setInputText(inputList[15])
        self.reversePage.clickFlipSentenceBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedFlipOneSentenceOutputList[15], actualResult, "Flip one sentence of string with only special characters"+ ", Expected:" + expectedFlipOneSentenceOutputList[15] + ", Actual:" + actualResult)

    def test_flipOneSentencecase17(self):
        self.reversePage.setInputText(inputList[16])
        self.reversePage.clickFlipSentenceBtn()
        actualResult = self.reversePage.getOutputText()
        self.assertEqual(expectedFlipOneSentenceOutputList[16], actualResult, "Flip one sentence of string with Chinese characters"+ ", Expected:" + expectedFlipOneSentenceOutputList[16] + ", Actual:" + actualResult)
    
    
    
    
    def tearDown(self):
        self.reversePage.setInputText("")
        
    @classmethod
    def tearDownClass(cls):
        getDriver().quit()

        
        
class TestFlipSentence(unittest.TestCase):
    pass
 
if __name__ == '__main__':
    
    unittest.main()
    