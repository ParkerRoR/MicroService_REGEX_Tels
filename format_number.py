
class Number:
    def formatar_n1(self, tel1):
        self.tel1 = tel1
        for i in range(len(self.tel1)):
            
            if (i == 0):
                pass
            else:
                #TELEFONE 1
                self.tel1[i] = self.tel1[i].replace('.0','')
                self.tel1[i] = self.tel1[i].replace(' ','')
                self.tel1[i] = self.tel1[i].replace('-','')
                self.tel1[i] = self.tel1[i].replace('(','')
                self.tel1[i] = self.tel1[i].replace(')','')
                self.tel1[i] = self.tel1[i].replace('?','')

                if (len(self.tel1[i]) == 10):
                    
                    for ddd in range(1, 99):
                        if (self.tel1[i][:2] == str(ddd)):
                            self.tel1[i] = self.tel1[i][2:]
                            self.tel1[i] = '{}9{}'.format(str(ddd),self.tel1[i])
                    if (self.tel1[i][:1] == '9'):
                        
                        self.tel1[i] = '21{}'.format(self.tel1[i][1:])

                elif(len(self.tel1[i]) == 9):
                    self.tel1[i] = '21{}'.format(self.tel1[i])
                    
                elif(self.tel1[i][:1] == '0'):
                    self.tel1[i] = self.tel1[i][1:]
                    
                elif(self.tel1[i][:2] == '55'):
                    self.tel1[i] = self.tel1[i][2:]
        return self.tel1