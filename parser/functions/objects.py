import os
import datetime
import shutil



class Backup():
    def copy(self, new_lines):
        if self.rep == True:
            with open(self.file, 'w') as file:
                for line in new_lines:
                    file.write(line)
                file.close()
        else:
            if len(os.path.dirname(self.file)) == 0:
                d = os.getcwd()

            else:
                d = os.path.dirname(self.file)

            if os.path.exists(d+ "/backup_" +os.path.basename(self.file)):
                source = self.file
                destination = d + "/" + str(datetime.datetime.now().timestamp()) + "_backup"+os.path.basename(self.file)

                shutil.copyfile(source, destination)
            else:
                source = self.file
                destination = d + "/backup_" + os.path.basename(self.file)

                shutil.copyfile(source, destination)
                
            with open(self.file, 'w') as file:
                for line in new_lines:
                    file.write(line)
                file.close()




class Parse(Backup):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        if self.case == "tabs":
            self.case = '\t'
            self.c = " "

        if self.case == "spaces":
            self.case = " "
            self.tabc = 1
            self.c = '\t'
            
    def parsing(self):
        times = 0
        if self.case != None:
            with open(self.file, 'r+') as temp_file:
                lines = temp_file.readlines()
                new_lines = []
                occur = 0
                for line in lines:
                    if line.startswith(self.case):
                        #Zamienia wszystkie tabulatory / spacje na początku linijki do momentu aż
                        #nie natrafi na znak sprzeczny z podanym parametrem --from
                        for i in range(0, len(line)):
                            if line[i] == self.case:
                                occur += 1
                            elif line[i] != self.case:
                                new_line = self.c * self.tabc * occur + line[occur:]
                                new_lines.append(new_line)
                                occur = 0
                                times += 1
                                break
                    else:
                        new_lines.append(line)
                temp_file.close()

                Backup.copy(self, new_lines)

        else:
            with open(self.file, 'r') as guess:
                tbs = 0
                spc = 0
                for line in guess:
                    if line[0] == '\t':
                        tbs +=1
                    else:
                        spc += 1
                guess.close()
                if tbs > spc:
                    print("File contains mostly tabs")
                elif spc > tbs:
                    print("File containts mostly spaces")
                else:
                    print("Same amount of spaces and tabs")


        print("Lines modified:", times)  



