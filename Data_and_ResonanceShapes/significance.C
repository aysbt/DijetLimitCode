#include <TString.h>
#include <TFile.h>
#include <TH1F.h>
#include <TMath.h>
void significance(){
using namespace std;   
    
    // Input Files
    TString dir = "";
    TFile *qcd = TFile::Open(dir+
                                   TString("QCD.root"), "READ");
    
    TFile *signal = TFile::Open(dir+
                                       TString("GG.root"), "READ");
	
    
    TH1F* h_qcd_nocut = (TH1F *) qcd->Get("h_QCD_nocut");
    TH1F* h_qcd_ld = (TH1F *) qcd->Get("h_QCD_bs_09");

    char *point = new char[100];
    char *point2 = new char[100];

    double res_mass[8] = {2000, 3000, 4000, 5000, 6000, 7000,8000,9000};

    for(int m=0; m<8; m++){
        
    sprintf(point,"h_M%d_nocut",res_mass[m]);
    sprintf(point2,"h_M%d_bs_09",res_mass[m]);
    // Histograms
    TH1F* h_signal_nocut = (TH1F *) signal->Get(point);
    TH1F* h_signal_ld = (TH1F *) signal->Get(point2);
    
    
    // Differantial Cross Section from data
    double sum_qcd(0.), sum_qcd_ld(0.), sum_signal(0.), sum_signal_ld(0.);
    int i;
    
    for(i=0;i<h_qcd_nocut->GetNbinsX();i++)
    {
        double mass        = h_qcd_nocut->GetBinCenter(i+1);
        double n_qcd       = h_qcd_nocut->GetBinContent(i+1);
        double n_qcd_ld    = h_qcd_ld->GetBinContent(i+1);
        double n_signal    = h_signal_nocut->GetBinContent(i+1);
        double n_signal_ld = h_signal_ld->GetBinContent(i+1);
       
        
        if (mass<1181)continue;
            
        if(mass>=res_mass[m]*0.9 && mass<=res_mass[m]*1.1)
		{
            sum_qcd = sum_qcd + n_qcd;
            sum_qcd_ld = sum_qcd_ld + n_qcd_ld;
            sum_signal = sum_signal + n_signal;
            sum_signal_ld = sum_signal_ld + n_signal_ld;
		}
        
    }
    
    double sig = sum_signal/sqrt(sum_qcd);
    double sig_ld = sum_signal_ld/sqrt(sum_qcd_ld);
        double imp = sig_ld/sig;
     
        cout<<imp<<", ";
 //   cout<<res_mass[m]<<endl;
 //   cout<<"Significance = "<<sig<<endl;
 //   cout<<"Significance after q/g tagging = "<<sig_ld<<endl;
 //   cout<<"Improvement = "<<sig_ld/sig<<endl;
 //   cout<<"========================"<<endl;
	}
}
