#include<iostream>
#include<fstream>
#include<map>
#include<algorithm>

using namespace std;
using PairSI=std::pair<std::string,int>;
bool lessValue(const PairSI &l,const PairSI &r)//there must be const &
{
    if(l.second<r.second)
        return true;
    else
        return false;

}
int statistics(std::istream& ifs)
{
    std::map<std::string,int> mp;
    //int cont=mp["wtlwang"];
    string s;
    while(ifs>>s)
    {
        mp[s]++;
    }
    auto it=std::max_element(mp.begin(),mp.end(),lessValue);
    cout<<"the max times element is: "<<endl;
    cout<<it->first<<" "<<it->second<<"times\n"<<endl;

    it=mp.begin();
    cout<<"the first element is: "<<endl;
    cout<<it->first<<" "<<it->second<<"times\n"<<endl;

    it=mp.end();
    it--;
    cout<<"the last element is: "<<endl;
    cout<<it->first<<" "<<it->second<<"times\n"<<endl;

    cout<<"the words are: "<<endl;
    for(auto p:mp)
    {
       cout<<p.first<<" "<<p.second<<"times"<<endl;
    }
    return 0;
}
int main(int argc,char * argv[])
{

    if(argc>1)
    {
         ifstream ifs(argv[1]);
         statistics(ifs);
    }
    else
    {
        statistics(std::cin);
    }



    //cout<<"the init value is: "<<cont<<endl;

}
