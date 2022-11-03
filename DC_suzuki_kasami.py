#!/usr/bin/env python
# coding: utf-8

# In[1]:


site_no=7              #random no chosen Sites numbered 0....6
print("{} sites in distributed system numbered 0...{}".format(site_no,site_no-1))
privileged_site=0      #site with token(random site chosen at start)
Site=[]
resp="START"


# In[2]:


class token:
    def __init__(self):
        self.queue=[]
        self.LN=[0]*site_no        


# In[3]:


class site:
    def __init__(self):
        self.RN=[0]*site_no
        self.is_privileged=0
        self.is_executing=0
        self.is_requesting=0
        
    def request_send(self,sender,sn):
        global Token
        global privileged_site
        self.RN[sender]=max(sn,self.RN[sender])
        if self.is_privileged:
            if (self.RN[sender]==Token.LN[sender]+1):
                Token.queue.append(sender)
            if (self.is_executing==0):
                self.is_privileged=0
                privileged_site=Token.queue.pop(0)
                
                


# In[4]:


def request_privilege(s_id):
    global Site
    global privileged_site
    if s_id>=site_no:
        print("Invalid Site ID")
        return
    Site[s_id].RN[s_id]+=1
    sn=Site[s_id].RN[s_id]
    if(Site[s_id].is_requesting==1 or Site[s_id].is_executing==1):
        print("SITE {} has already requested or is executing CS at the moment\n".format(s_id))
        return
    Site[s_id].is_requesting=1
    if privileged_site==s_id:
        Site[s_id].is_requesting=0
        Site[s_id].is_executing=1
        print("Site {} already has token and is entering CS".format(s_id))
        return
    else:
        for i in range(site_no):
            if i!=s_id:
                Site[i].request_send(s_id,sn)
    if privileged_site==s_id:
        Site[s_id].is_requesting=0
        Site[s_id].is_executing=1
        Site[s_id].is_privileged=1
        print("Site {} has received token and is entering CS".format(s_id))
    else:
        print("Site {} is executing CS and Site_{} has requested it".format(privileged_site,s_id))

    


# In[5]:


def display_state():
    global Token
    global Site
    print("\nDISPLAYING STATE OF THE SYSTEM\n------------------------")
    print("privileged_site : {}\n".format(privileged_site))
    print("TOKEN :")
    queue_state=Token.queue if len(Token.queue) else "empty"
    print("Token Queue : {}".format(queue_state))
    print("Token LN Array: {}".format(Token.LN))
    for i in range(site_no):
        print("S{}_RN Array :   {}".format(i,Site[i].RN))
    print("---------------------------\n")


# In[6]:


def release_CS(pid):
    global Token
    global privileged_site
    if pid>=site_no:
        print("Invalid Site ID")
        return
    if not Site[pid].is_executing:
        print("Site {} is not currently executing CS".format(pid))
        return
    Token.LN[pid]=Site[pid].RN[pid]
    Site[pid].is_executing=0
    print("Site {} has released CS\n".format(pid))
    if not len(Token.queue):
        print("No other site is requesting CS , token lies with the site {}\n".fomrat(pid))
    else:
        requester=Token.queue.pop(0)
        Site[pid].is_privileged=0
        privileged_site=requester
        Site[requester].is_privileged=1
        Site[requester].is_requesting=0
        Site[requester].is_executing=1
        print("Site {} has received the token and is entering CS\n".format(requester))


# In[7]:


def site_init():
    global Site
    for i in range(site_no):
        Site.append(site())


# In[ ]:


Token=token()
site_init()
Site[0].is_privileged=1     # choosing site 0 as holder of token in initial stage
display_state()
pid=0
while(1):
    print("\nPlease enter the operation\n1. Req for Requesting CS\n2. Rel for releasing CS\n3. End to terminate the program\n")
    resp=input()
    if resp=="Req":
        print("Enter Site id which is requesting CS\n")
        try:
            pid=input()
            pid=int(pid)
        except ValueError as val_e:
            print('\nEnter valid site_id\n')
            continue
        request_privilege(int(pid))
        display_state()
    elif resp=="Rel":
        print("Enter Site id which needs to exit CS\n")
        try:
            pid=input()
            pid=int(pid)
        except ValueError as val_e:
            print('\nEnter valid site_id\n')
            continue
        release_CS(int(pid))
        display_state()  
    elif resp=="End":
        break
    else:
        print('\nPlease enter a valid input\n')

