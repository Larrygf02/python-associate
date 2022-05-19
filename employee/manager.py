from employee import Employee

class Manager():

    def __init__(self, meeting=[]):
        self.meeting = meeting
    
    def schedule_meeting(self,invitees, time):
        data = {'invitees': invitees.split(","), "time": time}
        self.meeting.append(data)
        self.meeting = sorted(self.meeting, key=lambda m:m['time'])

    def run_next_meeting(self):
        if self.meeting:
            return self.meeting.pop()
        else:
            return "No more meetings"
        