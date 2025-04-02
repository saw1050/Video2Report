import whisper
import queue

class Transcribers:
    def __init__(self, model:str = 'large', devices:list[int] = None, num_work:int = 1):
        models = queue.Queue(max(len(devices)*num_work, 1))
        if devices is not None:
            for device in devices:
                for _ in range(num_work):
                    models.put(whisper.load_model(model, device=f'cuda:{device}'))
        else:
            for i in range(num_work):
                models.put(whisper.load_model(model))
        self.models = models
        
    def get_transcriber(self)->whisper.Whisper:
        return self.models.get(block=True, timeout=None)
    
    def return_transcriber(self, transcriber)->None:
        self.models.put(transcriber)
        
    def __len__(self)->int:
        return self.models.qsize()
    # def transcribe(self, video):
    #     return self.model.module.transcribe(video,fp16="False")
    
