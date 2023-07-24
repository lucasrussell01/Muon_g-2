#include "../include/RateEquation.h"

int solve_rateeq(double x,double y, double z,Mu muonium, Laser VUVlaser, Laser Unboundlaser,double vx, double *t_ion){
	RateEquationSolver *solver = new RateEquationSolver();
	solver->SetMuParameter(muonium.A12,muonium.B12,muonium.B21);
	solver->SetLaserParameter(VUVlaser);
	solver->SetIonizationLaserParameter(Unboundlaser);
	solver->SetMuPosition(z*1e-3,y*1e-3,x*1e-3);
	solver->SetMuVelocity( vx*1e-3 );
	
	if( (z*1e-3-VUVlaser.z_center)*(z*1e-3-VUVlaser.z_center)/VUVlaser.wz/VUVlaser.wz  +  (y*1e-3-VUVlaser.y_center)*(y*1e-3-VUVlaser.y_center)/VUVlaser.wy/VUVlaser.wy  < 2.5*2.5  ){ // solve the eq only for the particle within 2 sigma
		solver->Solve();
	}
	if(solver->Isionized()) {
		*t_ion = solver->GetIonTime();
		delete solver;
		return 1;
	}else{
		delete solver;
		return 0;
	}
}

double GetVx(double p, double xp, double yp){
	xp = xp/1000;
	yp = yp/1000;

	double mass_mu= 105.658; //MeV/C^2
	double mass_Mu =106.16;  // MeV/C^2
	double c=299792458;

	double Ekin = sqrt(p*p*1e3*1e3 + mass_mu*mass_mu)-mass_mu;  // MeV/C^2
	double V_Mu = sqrt(2*Ekin/mass_Mu)*c;
	double vz = V_Mu/sqrt(1 + xp*xp + yp*yp); // m/s

	return vz*xp*1e3;  // mm/s
}

double GetVy(double p, double xp, double yp){
	xp = xp/1000;
	yp = yp/1000;

	double mass_mu= 105.658; //MeV/C^2
	double mass_Mu =106.16;  // MeV/C^2
	double c=299792458;

	double Ekin = sqrt(p*p*1e3*1e3 + mass_mu*mass_mu)-mass_mu;  // MeV/C^2
	double V_Mu = sqrt(2*Ekin/mass_Mu)*c;
	double vz = V_Mu/sqrt(1 + xp*xp + yp*yp); // m/s

	return vz*yp*1e3;  // mm/s
}

double GetVz(double p, double xp, double yp){
	xp = xp/1000;
	yp = yp/1000;

	double mass_mu= 105.658; //MeV/C^2
	double mass_Mu =106.16;  // MeV/C^2
	double c=299792458;

	double Ekin = sqrt(p*p*1e3*1e3 + mass_mu*mass_mu)-mass_mu;  // MeV/C^2
	double V_Mu = sqrt(2*Ekin/mass_Mu)*c;
	double vz = V_Mu/sqrt(1 + xp*xp + yp*yp); // m/s

	return vz*1e3;  // mm/s
}

int ReadVUVparameters(Laser *vuv,const string filename="VUVparam.txt"){
	ifstream ifs(filename);
	double param[10];
	double tmp;
	int i=0;
	while(ifs>>tmp){
		param[i]=tmp;
		i+=1;
	}

	vuv->energy=param[0];
	vuv->wz=param[1];
	vuv->wy=param[2];
	vuv->z_center=param[3];
	vuv->y_center=param[4];
	vuv->l_FHWM = param[5]; 
	vuv->detune = param[6];
	vuv->t_center = param[7];
	vuv->t_sigma = param[8]/2.35;
	//if( argc >9){ filename = argv[9]; } 
	
	ifs.close();

	return 0;
}
int ReadUnboundLaserparameters(Laser *unbound,const string filename="Unboundparam.txt"){
	ifstream ifs(filename);
	double param[10];
	double tmp;
	int i=0;
	while(ifs>>tmp){
		param[i]=tmp;
		i+=1;
	}

	unbound->energy=param[0];
	unbound->wz=param[1];
	unbound->wy=param[2];
	unbound->z_center=param[3];
	unbound->y_center=param[4];
	unbound->l_FHWM = param[5]; 
	unbound->detune = param[6];
	unbound->t_center = param[7];
	unbound->t_sigma = param[8]/2.35;
	
	ifs.close();

	return 0;
}

int main(int argc, char** argv){
	TString filename = "data/MuYield_220128_2e6_010000_focus05_366007_tree_Type1002_D87000_T322_Nrepeat140317_H_line1_Thick7.12_NewGeo0_ionization_1.35_2630.dat";
	Mu muonium;
	Laser VUVlaser;
	Laser Unboundlaser;

	if( argc >1){ filename = argv[1]; } 
	ifstream ifs(filename.Data());
	TString fout = filename + "_ion.txt";
	if( argc >2){ fout = argv[2]; } 
	ofstream ofs(fout.Data());

	//TApplication theApp("waveview", &argc, argv);
	//gROOT->Macro("~/rootlogon.C");

	double ion_tot = 0;
	double x,y,z,vx,vy,vz,xp,yp,p,dummy1,dummy2,dummy3, dummy4;
	int j = 0;


	ReadVUVparameters(&VUVlaser);
	ReadUnboundLaserparameters(&Unboundlaser);

	while(ifs>> x >> xp >> y >> yp >> p >> z >> dummy1>>dummy2>>dummy3>>dummy4 ){
		double t_ion=0;
		vx= GetVx(p,xp,yp); 
		vy= GetVy(p,xp,yp); 
		vz= GetVz(p,xp,yp); 
		if(solve_rateeq(x*10,y*10,z,muonium,VUVlaser,Unboundlaser,vx,&t_ion) ==1 ){
			ion_tot+=1;
			ofs <<setprecision(6)<< x<<"	"<<xp<<"	"<<y<<"	"<<yp<<"	"<<scientific<< p<<"	"<< fixed <<z<<"	"<< t_ion*1e9 <<"	"<<setprecision(0) <<dummy2<<"	"<<dummy3<<"	"<< fixed<< dummy4<< endl;
		}
		j+=1;
	}
	// For marameter scan -> Save result
	cout << ion_tot/j <<"	"<< j<< endl;

	const char *filename_tmp = "eff_temp.txt";
	ofstream writing_file(filename_tmp);
	writing_file << ion_tot/j <<"	"<< VUVlaser.energy <<endl;
	writing_file.close();
	//
	ofs.close();

	return 0;

}

