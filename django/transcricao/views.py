import whisper

from django.http import HttpResponse
from django.views.generic.edit import FormView

from transcricao.forms import TranscricaoForm


class TranscricaoView(FormView):
    template_name = "transcricao/index.html"
    form_class = TranscricaoForm
    success_url = "."

    def form_valid(self, form):
        # Salvar o arquivo temporariamente
        with open('temp_audio.mp3', 'wb') as temp_audio:
            for chunk in form.cleaned_data["arquivo"].chunks():
                temp_audio.write(chunk)

        model = whisper.load_model("small")
        result = model.transcribe("temp_audio.mp3")

        return HttpResponse(result["text"], content_type='text/plain')

        return super().form_valid(form)
