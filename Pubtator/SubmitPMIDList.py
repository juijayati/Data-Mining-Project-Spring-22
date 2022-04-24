import requests
import io
import json
import sys
import time
import xmltodict


def SubmitPMIDList(Inputfile,Format,Bioconcept):
        
        jsonn = {}
        
        #
        # load pmids
        #
        with io.open(Inputfile,'r',encoding="utf-8") as file_input:
                jsonn = {"pmids": [pmid.strip() for pmid in file_input.readlines()]}
        #
        # load bioconcepts
        #
##        jsonn={"pmids":[19128254,29601617,27828635]}
        jsonn["concepts"]=Bioconcept.split(",")
                
        #
        # request
        #
        r = requests.post("https://www.ncbi.nlm.nih.gov/research/pubtator-api/publications/export/"+Format , json = jsonn)
        if r.status_code != 200 :
                print ("[Error]: HTTP code "+ str(r.status_code))
        else:
                count=0
                ff=open("log.xml","wb")
                ff.write(r.text.encode("utf-8"))
                ff.close()
                with open("log.xml",encoding="utf-8") as xml_file:
                        data_dict=xmltodict.parse(xml_file.read())
                xml_file.close()
                json_data=json.dumps(data_dict)
##                print(json_data)
                objs=json.loads(json_data)
                fi=open("annotatedabstracts.txt","a")
                for ob in range(0,len(objs["collection"]["document"])):
##                        print(objs["collection"]["document"][1]["passage"][1]["annotation"])
                        try:
                                line=objs["collection"]["document"][ob]["passage"][1]["text"]
                                offset=int(objs["collection"]["document"][ob]["passage"][1]["offset"])-1
##                                print(line)
                                for xx in objs["collection"]["document"][ob]["passage"][1]["annotation"]:
        ##                                print(xx['@id'])
                                        line=line.replace(objs["collection"]["document"][ob]["passage"][1]["text"][int(xx['location']['@offset'])-offset-1:int(xx['location']['@offset'])+int(xx['location']['@length'])-offset],"GENE:"+xx['infon'][0]['#text'])
##                                        print(xx['infon'][0]['#text'])
##                                        print(xx['location']['@offset'])
##                                        print(xx['location']['@length'])
                                lines=line.split(".")
                                flag=0
                                for line in lines:
                                        if("GENE" in line):
                                                fi.write(line+".")
                                                flag=1
                                if(flag==1):
                                        fi.write("\n")
##                                        print(line)
                        except:
                                count+=1;
                fi.close()
                print("err count")
                print(count);

if __name__ == "__main__":

##      if arg_count<2 or (sys.argv[2]!= "pubtator" and sys.argv[2]!= "biocxml" and sys.argv[2]!= "biocjson"):
##              print("\npython SubmitPMIDList.py [InputFile] [Format] [BioConcept]\n\n")
##              print("\t[Inputfile]: a file with a pmid list\n")
##              print("\t[Format]: pubtator (PubTator), biocxml (BioC-XML), and biocjson (JSON-XML)\n")
##              print("\t[Bioconcept]: gene, disease, chemical, species, proteinmutation, dnamutation, snp, and cellline. Default includes all.\n")
##              print("\t* All input are case sensitive.\n\n")
##              print("Eg., python SubmitPMIDList.py examples/ex.pmid pubtator gene,disease\n\n")
##      else:
        Format = "biocxml"
        Bioconcept="gene"
        for i in range(0,8601,100):
                print("i is ",i)
                Inputfile="pmid"+str(i)+".txt"
                SubmitPMIDList(Inputfile,Format,Bioconcept)
                time.sleep(0.5)
