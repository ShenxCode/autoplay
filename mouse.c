#include <stdio.h>
#include <winuser.h>
#include <Windows.h>
#include <time.h>
//消息队列

INPUT * creat_mouse_input(void);




int main()
{
    INPUT * ip; 
    ip=creat_mouse_input();
    ip->mi.dwFlags|=MOUSEEVENTF_MOVE|MOUSEEVENTF_LEFTDOWN|MOUSEEVENTF_LEFTUP;
    ip->mi.dx=(65535/1900)*651;
    ip->mi.dy=(65535/1080)*442;

    SendInput(1,ip,sizeof(INPUT));
    ip->mi.dwFlags=MOUSEEVENTF_LEFTDOWN;
    SendInput(1,ip,sizeof(INPUT));
    ip->mi.dwFlags=MOUSEEVENTF_LEFTUP;
    SendInput(1,ip,sizeof(INPUT));

    free(ip);
    return 0;
}

INPUT * creat_mouse_input(void)
{
    INPUT * ip=NULL;
    ip=(INPUT *)malloc(sizeof(INPUT));
    ip->type=INPUT_MOUSE;
    ip->mi.dx=0;
    ip->mi.dy=0;
    ip->mi.dwFlags=MOUSEEVENTF_ABSOLUTE;
    ip->mi.dwExtraInfo=0;
    ip->mi.mouseData=0;
    ip->mi.time=0;
    return ip;
}