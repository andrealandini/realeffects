import numpy as np
from math import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.style.use("ggplot")


class DB:
    def __init__(self):

        self.k = 1
        self.qì = 6
        self.chi = .4
        self.d = np.linspace(0,self.chi*self.qì*self.k,1000)


        self.beta_b = .6
        self.y1b = 10
        self.y2b = 11
        self.q = 5
        #db = (d*(1+beta_b)+beta_b*(y1b-q*k))**(-1)*(y2b+qì*k)
        self.db = np.piecewise(self.d, [self.d < self.chi*self.qì*self.k, self.d >= self.chi*self.qì*self.k],
                        [lambda x: (self.qì*self.k+self.y2b)/(x*(1+self.beta_b)+self.beta_b*(self.y1b-self.q*self.k)), 0])


        self.beta_s = .7
        self.y1s = 10
        self.y2s = 11
        self.s = np.linspace(0,self.beta_s*self.y1s/(1+self.beta_s)-.1,100)

        self.ds = (self.beta_s*self.y1s-self.s*(1+self.beta_s))**(-1)*self.y2s


        fig = plt.figure(figsize=(16,9))#fig, ax = plt.subplots(1, 2,figsize=(12, 8))
        fig.suptitle('DB Real Effects', fontsize=30)
        ax1 = fig.add_subplot(2, 4, 1)
        ax2 = fig.add_subplot(2, 4, 2)
        ax3 = fig.add_subplot(2, 4, 3)

        ax4 = fig.add_subplot(1, 4, 4)

        ax5 = fig.add_subplot(2, 4, 7)
        ax6 = fig.add_subplot(2, 4, 5)
        ax7 = fig.add_subplot(2, 4, 6)


        for x in [ax1,ax2,ax3,ax4,ax5,ax6,ax7]:
            #print("lesgo")
            x.plot(self.d,self.db,"purple",alpha=.3)
            x.plot(self.s,self.ds,"orange")
            x.set_xlim(0,self.chi*self.qì*self.k+2)
            x.set_ylim(min(self.db),max(self.db))




        self.p1, = ax1.plot([], [],color="red")
        self.time_text1 = ax1.text(.26, 0.9,'', transform=ax1.transAxes)
        ax1.text(.14, 0.9,'$y_{1}^b$ =', transform=ax1.transAxes)

        self.p2, = ax2.plot([], [],color="blue")
        self.time_text2 = ax2.text(.26, 0.9,'', transform=ax2.transAxes)
        ax2.text(.14, 0.9,'$y_{2}^b$ =', transform=ax2.transAxes)

        self.p6, = ax6.plot([], [],color="red")
        self.time_text6 = ax6.text(.26, 0.9,'', transform=ax6.transAxes)
        ax6.text(.14, 0.9,'$\\beta^b$ =', transform=ax6.transAxes)

        self.p4, = ax4.plot([], [],color="k")
        self.time_text4 = ax4.text(.26, 0.9,'', transform=ax4.transAxes)
        ax4.text(.14, 0.9,'$\chi$ =', transform=ax4.transAxes)

        self.p5, = ax5.plot([], [],color="green")
        self.time_text5 = ax5.text(.26, 0.9,'', transform=ax5.transAxes)
        ax5.text(.14, 0.9,'$q\'$ =', transform=ax5.transAxes)

        self.p3, = ax3.plot([], [],color="green")
        self.time_text3 = ax3.text(.26, 0.9,'', transform=ax3.transAxes)
        ax3.text(.14, 0.9,'$k$ =', transform=ax3.transAxes)

        self.p7, = ax7.plot([], [],color="blue")
        self.time_text7 = ax7.text(.26, 0.9,'', transform=ax7.transAxes)
        ax7.text(.14, 0.9,'$q$ =', transform=ax7.transAxes)








        self.animation = animation.FuncAnimation(
            fig, self.update, frames=range(0,1000), interval=10, blit=True)

    def update(self,i):
        y1b = np.linspace(8,16,1000)
        y2b = np.linspace(9,17,1000)
        beta_b = np.linspace(.1,1,1000)
        chi = np.linspace(.1,.73,1000)
        qì = np.linspace(5.5,9,1000)
        k = np.linspace(.1,1.5,1000)
        q = np.linspace(4.5,8,1000)

        d4 = np.linspace(0, chi[i]*self.qì*self.k, 1000)
        d5 = np.linspace(0, self.chi*qì[i]*self.k, 1000)
        d6 = np.linspace(0, self.chi*self.qì*k[i], 1000)

        #self.y2b = np.linspace(8,16,1000)
        #self.y2b = np.linspace(8,12,1000)

        self.p1.set_xdata(self.d)
        self.p1.set_ydata(np.piecewise(self.d, [self.d < self.chi*self.qì*self.k, self.d >= self.chi*self.qì*self.k],
                        [lambda x: (self.qì*self.k+self.y2b)/(x*(1+self.beta_b)+self.beta_b*(y1b[i]-self.q*self.k)), 0]))
        self.time_text1.set_text(round(y1b[i],3))


        self.p2.set_xdata(self.d)
        self.p2.set_ydata(np.piecewise(self.d, [self.d < self.chi*self.qì*self.k, self.d >= self.chi*self.qì*self.k],
                        [lambda x: (self.qì*self.k+y2b[i])/(x*(1+self.beta_b)+self.beta_b*(self.y1b-self.q*self.k)), 0]))
        self.time_text2.set_text(round(y2b[i],3))


        self.p6.set_xdata(self.d)
        self.p6.set_ydata(np.piecewise(self.d, [self.d < self.chi*self.qì*self.k, self.d >= self.chi*self.qì*self.k],
                        [lambda x: (self.qì*self.k+self.y2b)/(x*(1+beta_b[i])+beta_b[i]*(self.y1b-self.q*self.k)), 0]))
        self.time_text6.set_text(round(beta_b[i],3))


        #self.p4.set_xdata(np.linspace(0, max(chi)*self.qì*self.k, 1000))
        self.p4.set_xdata(d4)
        self.p4.set_ydata(np.piecewise(d4, [d4 < chi[i]*self.qì*self.k, d4 >= chi[i]*self.qì*self.k],
                        [lambda x: (self.qì*self.k+self.y2b)/(x*(1+self.beta_b)+self.beta_b*(self.y1b-self.q*self.k)), 0]))
        self.time_text4.set_text(round(chi[i],3))


    
        #d5 = self.p5.set_xdata(np.linspace(0, self.chi*max(qì)*self.k, 1000))
        self.p5.set_xdata(d5)
        self.p5.set_ydata(np.piecewise(d5, [d5 < self.chi*qì[i]*self.k, d5 >= self.chi*qì[i]*self.k],
                        [lambda x: (qì[i]*self.k+self.y2b)/(x*(1+self.beta_b)+self.beta_b*(self.y1b-self.q*self.k)), 0]))
        self.time_text5.set_text(round(qì[i],3))


        #self.p6.set_xdata(np.linspace(0, self.chi*self.qì*max(k), 1000))
        self.p3.set_xdata(d6)
        self.p3.set_ydata(np.piecewise(d6, [d6 < self.chi*self.qì*k[i], d6 >= self.chi*self.qì*k[i]],
                        [lambda x: (self.qì*k[i]+self.y2b)/(x*(1+self.beta_b)+self.beta_b*(self.y1b-self.q*k[i])), 0]))
        self.time_text3.set_text(round(k[i],3))


        self.p7.set_xdata(self.d)
        self.p7.set_ydata(np.piecewise(self.d, [self.d < self.chi*self.qì*self.k, self.d >= self.chi*self.qì*self.k],
                        [lambda x: (self.qì*self.k+self.y2b)/(x*(1+self.beta_b)+self.beta_b*(self.y1b-q[i]*self.k)), 0]))
        self.time_text7.set_text(round(q[i],3))



        return (self.p1, self.time_text1, 
                self.p2, self.time_text2,
                self.p3, self.time_text3, 
                self.p4, self.time_text4,
                self.p5, self.time_text5, 
                self.p6, self.time_text6,
                self.p7, self.time_text7,)


class DS:
    def __init__(self):

        self.k = 1
        self.qì = 6
        self.chi = .4
        self.d = np.linspace(0,self.chi*self.qì*self.k,1000)


        self.beta_b = .6
        self.y1b = 10
        self.y2b = 11
        self.q = 5
        #db = (d*(1+beta_b)+beta_b*(y1b-q*k))**(-1)*(y2b+qì*k)
        self.db = np.piecewise(self.d, [self.d < self.chi*self.qì*self.k, self.d >= self.chi*self.qì*self.k],
                        [lambda x: (self.qì*self.k+self.y2b)/(x*(1+self.beta_b)+self.beta_b*(self.y1b-self.q*self.k)), -10])


        self.beta_s = .7
        self.y1s = 10
        self.y2s = 11
        self.s = np.linspace(0,self.beta_s*self.y1s/(1+self.beta_s)-.1,100)

        self.ds = (self.beta_s*self.y1s-self.s*(1+self.beta_s))**(-1)*self.y2s


        fig = plt.figure(figsize=(16,9))#fig, ax = plt.subplots(1, 2,figsize=(12, 8))
        fig.suptitle('DS Real Effects', fontsize=30)
        ax1 = fig.add_subplot(1, 3, 1)
        ax2 = fig.add_subplot(1, 3, 2)
        ax3 = fig.add_subplot(1, 3, 3)



        for x in [ax1,ax2,ax3]:
            #print("lesgo")
            x.plot(self.d,self.db,"purple",alpha=.3)
            x.plot(self.s,self.ds,"orange")
            x.set_xlim(0,self.chi*self.qì*self.k+2.5)
            #x.set_ylim(min(self.ds),max(self.db))




        self.p1, = ax1.plot([], [],color="k")
        self.time_text1 = ax1.text(.26, 0.9,'', transform=ax1.transAxes)
        ax1.text(.14, 0.9,'$y_{1}^s$ =', transform=ax1.transAxes)

        self.p2, = ax2.plot([], [],color="k")
        self.time_text2 = ax2.text(.26, 0.9,'', transform=ax2.transAxes)
        ax2.text(.14, 0.9,'$y_{2}^s$ =', transform=ax2.transAxes)

        self.p3, = ax3.plot([], [],color="k")
        self.time_text3 = ax3.text(.26, 0.9,'', transform=ax3.transAxes)
        ax3.text(.14, 0.9,'$\\beta^s$ =', transform=ax3.transAxes)








        self.animation = animation.FuncAnimation(
            fig, self.update, frames=range(0,1000), interval=10, blit=True)

    def update(self,i):
        y1s = np.linspace(8,16,1000)
        y2s = np.linspace(9,17,1000)
        beta_s = np.linspace(.1,1,1000)
      
        s1 = np.linspace(0,self.beta_s*y1s[i]/(1+self.beta_s)-.1,100)
        s3 = np.linspace(0,beta_s[i]*self.y1s/(1+beta_s[i])-.1,100)




        self.p1.set_xdata(s1)
        self.p1.set_ydata((self.beta_s*y1s[i]-s1*(1+self.beta_s))**(-1)*self.y2s)
        self.time_text1.set_text(round(y1s[i],3))


        self.p2.set_xdata(self.s)
        self.p2.set_ydata((self.beta_s*self.y1s-self.s*(1+self.beta_s))**(-1)*y2s[i])
        self.time_text2.set_text(round(y2s[i],3))


        self.p3.set_xdata(s3)
        self.p3.set_ydata((beta_s[i]*self.y1s-s3*(1+beta_s[i]))**(-1)*self.y2s)
        self.time_text3.set_text(round(beta_s[i],3))





        return (self.p1, self.time_text1, 
                self.p2, self.time_text2,
                self.p3, self.time_text3,)








ani_db = DB().animation
ani_ds = DS().animation


#ani_db.save("MOGUSDB.mp4")
#ani_ds.save("MOGUSDS.mp4")
plt.show()