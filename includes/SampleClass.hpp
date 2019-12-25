#ifndef _SAMPLECLASS_HPP_INCLUDE_
#define _SAMPLECLASS_HPP_INCLUDE_
#pragma pack(1) 
struct sRawStructCurve
{
    short m_classid;
    char m_majorNSV;
    char m_minorNSV;
    int m_classSize;
};
#pragma pack() 
class Curve
{
public:
    Curve() : m_ptr(&m_curve){ memset(m_ptr, 0, sizeof(m_curve)); };
    Curve(void* ptr) : m_ptr(ptr){ };
    short getclassid(){ return m_ptr->m_classid; }
    void setclassid(const short& val){ m_ptr->m_classid = val; }
    char getmajorNSV(){ return m_ptr->m_majorNSV; }
    void setmajorNSV(const char& val){ m_ptr->m_majorNSV = val; }
    char getminorNSV(){ return m_ptr->m_minorNSV; }
    void setminorNSV(const char& val){ m_ptr->m_minorNSV = val; }
    int getclassSize(){ return m_ptr->m_classSize; }
    void setclassSize(const int& val){ m_ptr->m_classSize = val; }
protected:
    sRawStructCurve* m_ptr;
    sRawStructCurve m_curve;
};
#endif _SAMPLECLASS_HPP_INCLUDE_
