def solution(video_len, pos, op_start, op_end, commands):
    full_video_time=int(video_len[0:2])*60+int(video_len[3:])
    now_time=int(pos[0:2])*60+int(pos[3:])
    opening_start=int(op_start[0:2])*60+int(op_start[3:])
    opening_end=int(op_end[0:2])*60+int(op_end[3:])
    if opening_start<=now_time<=opening_end:
            now_time=opening_end
    for x in commands:
        
        if x=="prev":
            now_time=0 if now_time-10<0 else now_time-10
        else:
            now_time=full_video_time if now_time+10>full_video_time else now_time+10
        
        if opening_start<=now_time<=opening_end:
            now_time=opening_end
    m,s=str(now_time//60),str(now_time%60)
    return f'{"0"+m if len(m)==1 else m}:{"0"+s if len(s)==1 else s}