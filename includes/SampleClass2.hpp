#ifndef _SAMPLECLASS2_HPP_INCLUDE_
#define _SAMPLECLASS2_HPP_INCLUDE_
#pragma pack(1) 
struct sRawStructCurve1
{
    short m_classid;
    char m_majorNSV;
    char m_minorNSV;
    int m_classSize;
};
#pragma pack() 
class Curve1
{
public:
    Curve1() : m_ptr(&m_curve1){ memset(m_ptr, 0, sizeof(m_curve1)); };
    Curve1(void* ptr) : m_ptr(ptr){ };
    short getclassid(){ return m_ptr->m_classid; }
    void setclassid(const short& val){ m_ptr->m_classid = val; }
    char getmajorNSV(){ return m_ptr->m_majorNSV; }
    void setmajorNSV(const char& val){ m_ptr->m_majorNSV = val; }
    char getminorNSV(){ return m_ptr->m_minorNSV; }
    void setminorNSV(const char& val){ m_ptr->m_minorNSV = val; }
    int getclassSize(){ return m_ptr->m_classSize; }
    void setclassSize(const int& val){ m_ptr->m_classSize = val; }
protected:
    sRawStructCurve1* m_ptr;
    sRawStructCurve1 m_curve1;
};
#endif _SAMPLECLASS2_HPP_INCLUDE_
