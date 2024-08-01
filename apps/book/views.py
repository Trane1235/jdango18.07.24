from django.shortcuts import render


class CakeView(TemplataView):
    template_name = 'cakes/index.html'
    def get_context_date(self, **kwargs):
        context = super(
            CakeView, self
        ).get_context_data(**kwrgs)

        context['itemes'] = ['img/cake.jpg',]
        return context

