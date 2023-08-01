const string filename = "~/ToRFQstudy/run/data/musr_14015.root";

const string draw = "save_px/save_pz:save_x-780";
const string cut  = "save_detID==654&&save_particleID==-13";

TFile* fF;
TTree* fT;

const int    xnbin = 60;
const double xmin  = -12;
const double xmax  = 12;
const int    ynbin = 60;
const double ymin  = -0.12;
const double ymax  = 0.12;


TCut Xacceptance_cut = "0.0148368*(-1.0745*(save_x-780)+TMath::Sqrt(1.15455*(save_x-780)*(save_x-780)-67.4*(-0.0835+0.0319666*(save_x-780)*(save_x-780))))>save_px/save_pz"; 
TCut Xacceptance_cut2 = "0.0148368*(-1.0745*(save_x-780) -TMath::Sqrt(1.15455*(save_x-780)*(save_x-780)-67.4*(-0.0835+0.0319666*(save_x-780)*(save_x-780))))<save_px/save_pz"; 
TCut Yacceptance_cut =  "0.0148368*(-1.0745*save_y+TMath::Sqrt(1.15455*save_y*save_y-67.4*(-0.0835+0.0319666*save_y*save_y)))>save_py/save_pz";
TCut Yacceptance_cut2 =  "0.0148368*(-1.0745*save_y - TMath::Sqrt(1.15455*save_y*save_y-67.4*(-0.0835+0.0319666*save_y*save_y)))<save_py/save_pz";
TCut detector_cut = cut.c_str(); 

fout="macro/soa_sim_result.txt";

double alpha = 1.0745;
double beta = 0.06740*100               *10;
double epsilon = 0.167*5.0*1e-4/0.01    *10;

void EditTH2F(TH2F *h2,const char *title, const char *xtitle,const char *ytitle){
    h2->SetXTitle(xtitle);
    h2->SetYTitle(ytitle);
    h2->SetTitle(title);
}


void SetTH2FRange(TH2F *h2, double xmin, double xmax, double ymin, double ymax){
    h2->GetXaxis()->SetRangeUser(xmin,xmax);
    h2->GetYaxis()->SetRangeUser(ymin,ymax);
}


void EditTH1F(TH1F *h2,const char *title, const char *xtitle,const char *ytitle){
    h2->SetXTitle(xtitle);
    h2->SetYTitle(ytitle);
    h2->SetTitle(title);
}


void SetTH1FRange(TH1F *h2, double xmin, double xmax, double ymin, double ymax){
    h2->GetXaxis()->SetRangeUser(xmin,xmax);
    h2->GetYaxis()->SetRangeUser(ymin,ymax);
}

TString GetSavename(TString fin){
    int len = fin.Length();
    TString s_temp = fin(5,len-5-5);  // first 5 is "data/" , second 5 is ".root"
    TString s = "fig/" + s_temp + ".pdf";
    cout << s << endl;
    return s;
}


void DrawSimResult(const string filename_input="",double Mutot=0){

    gROOT->Macro("~/rootlogon.C");
    TCanvas* c1 = new TCanvas("c1","c1",1500,1000);
    c1->Divide(3,2);
    gStyle->SetOptStat(1110);
   
    TF1* env3(string name, double a2, double b2, double e2);
    TF1* env4(string name, double a2, double b2, double e2);
    TF1* up2   = env3("up2", alpha,beta,epsilon);
    TF1* down2 = env4("down2", alpha,beta,epsilon);

	if(filename_input.length()==0){
		fF = new TFile(filename.c_str(), "read");
	} else {
		fF = new TFile(filename_input.c_str(), "read");
	} 
    fT = (TTree*)fF->Get("t1");
	if(Mutot==0){Mutot=fT->GetEntries();}
    cout << fT->GetEntries() <<endl;
    c1->cd(1);
    TH2F*  fH_x= new TH2F("fH_x","",xnbin, xmin, xmax, ynbin, ymin, ymax);
    //fT->Draw("save_px/save_pz:save_x-780 >> fH_x",( Xacceptance_cut && Xacceptance_cut2 && Yacceptance_cut && Yacceptance_cut2  ) && detector_cut,"colz");
    //fT->Draw("save_px/save_pz:save_x-780 >> fH_x",( Xacceptance_cut && Xacceptance_cut2 ) && detector_cut,"colz");
    //fT->Draw("save_px/save_pz:save_x-780 >> fH_x",Yacceptance_cut && Xacceptance_cut && detector_cut,"colz");
    fT->Draw("save_px/save_pz:save_x-780 >> fH_x",detector_cut,"colz");
    EditTH2F(fH_x,"x","x [mm]","x' [rad]");
    SetTH2FRange(fH_x,xmin,xmax,ymin,ymax);
    fH_x->Draw("colz");
    up2->Draw("same");
    down2->Draw("same");
 
 
    c1->cd(2);
    TH2F *fH_y = new TH2F("fH_y","fH_y",xnbin, xmin, xmax, ynbin, ymin, ymax);
    //fT->Draw("save_py/save_pz:save_y >> fH_y",( Xacceptance_cut && Xacceptance_cut2 && Yacceptance_cut && Yacceptance_cut2  ) && detector_cut,"colz");
    fT->Draw("save_py/save_pz:save_y >> fH_y",cut.c_str(), "colz");
    EditTH2F(fH_y,"y","y [mm]","y' [rad]" );
    SetTH2FRange(fH_y,xmin,xmax,ymin,ymax);
    fH_y->Draw("colz");
    up2->Draw("same");
    down2->Draw("same");
    
    c1->cd(3);
    TH2F *fH_prof = new TH2F("fH_prof","fH_prof",xnbin, -7, 7, ynbin,-7, 7);
    //fT->Draw("save_y:save_x-780>> fH_prof",( Xacceptance_cut && Xacceptance_cut2 && Yacceptance_cut && Yacceptance_cut2  ) && detector_cut,"colz");
    fT->Draw("save_y:save_x-780 >> fH_prof",cut.c_str(), "colz");
    EditTH2F(fH_prof,"xy profile","x [mm]","y [mm]" );
    fH_prof->Draw("colz");

    c1->cd(4);
    TH1F *fH_time = new TH1F("fH_time","fH_time",200,300,500);
    //TH1F *fH_time = new TH1F("fH_time","fH_time",xnbin,460,500);
    fT->Draw("det_time_start*1000  >> fH_time",cut.c_str(),"");
    EditTH1F(fH_time,"timing profile","time [ns]","Entry" );
    fH_time->Draw();
    
    c1->cd(5);
    //TH1F *fH_tof = new TH1F("fH_tof","fH_tof",xnbin,460,500);
    //fT->Draw("det_time_start*1000 - muIniTime*1000   >> fH_tof",cut.c_str(),"");
    //EditTH1F(fH_tof,"TOF","time [ns]","Entry" );
    //fH_tof->Draw();
    TH1F *fH_kin = new TH1F("fH_kin","fH_kin",xnbin,2,6);
    fT->Draw("save_ke*1e3   >> fH_kin",cut.c_str(),"");
    EditTH1F(fH_kin,"Energy","Energy [keV]","Entry" );
    fH_kin->Draw();

    //int IsAccel = fT->GetEntries(Yacceptance_cut && Xacceptance_cut && detector_cut  );
    double IsAccel = fT->GetEntries(Yacceptance_cut && Yacceptance_cut2 &&  Xacceptance_cut && Xacceptance_cut2 && detector_cut  );

    c1->cd(6);
    double p1=0;
    TText *t = new TText(0.5, 0.5, "");
    t->DrawTextNDC(0.2, 0.75, Form("# of particle inside RFQ is %.3f", IsAccel/Mutot));

    TText *t_decay = new TText(0.5, 0.5, "");
    t_decay->DrawTextNDC(0.2, 0.65, Form("# of particle do not reach RFQ is %.3f", 1- (double)fT->GetEntries(detector_cut)/Mutot));

    //TText *t_decay_expect = new TText(0.5, 0.5, "");
    //t_decay_expect->DrawTextNDC(0.2, 0.55, Form("  expected decay loss is %.3f",1 - exp(-1* fH_tof->GetMean() /2.2e3) ) );

    cout << "# of particle inside RFQ acceptance is " << IsAccel/Mutot << endl;


	ofstream ofs(fout);
	double kin_mean = IsAccel/Mutot>0?fH_kin->GetMean():1000;
	double t_sigma = IsAccel/Mutot>0?fH_time->GetRMS():1000;
	ofs << IsAccel/Mutot <<"\t" << kin_mean <<"\t"<< t_sigma<<"\t"<< fH_kin->GetEntries()   <<endl; 
	ofs.close();

    if(filename_input.length()!=0){ c1->Print(GetSavename(filename_input));}
    c1->Print("fig/Allfig.pdf");
    c1->Print("fig/Allfig.png");
}

TF1* env3(string name, double a2, double b2, double e2){
    double c2 = (1.0+a2*a2)/b2;
    Char_t func[200];
    sprintf(func,"1./%lf*(-1.*%lf*x+TMath::Sqrt(%lf*%lf*x*x-%lf*(%lf*x*x-%lf)))",b2,a2,a2,a2,b2,c2,e2);
    TF1 *f = new TF1(name.c_str(),func,-1.*TMath::Sqrt(b2*e2),TMath::Sqrt(b2*e2));//最後の２つは最小と最大
    return f;
}
TF1* env4(string name, double a2, double b2, double e2){
    double c2 = (1.0+a2*a2)/b2;
    Char_t func[200];
    sprintf(func,"1./%lf*(-1.*%lf*x-TMath::Sqrt(%lf*%lf*x*x-%lf*(%lf*x*x-%lf)))",b2,a2,a2,a2,b2,c2,e2);
    TF1 *f = new TF1(name.c_str(),func,-1.*TMath::Sqrt(b2*e2),TMath::Sqrt(b2*e2));
    return f;
}














