from django.shortcuts import  get_object_or_404,render,redirect
from django.template import loader
from django.utils import timezone
from django.urls import reverse
from .models import Post,Question,Choice
from django.http import HttpResponse,HttpResponseRedirect
from .forms import BasicForm


# Create your views here.


def list(request):
	posts = Post.objects.order_by('-published_date')[:5]
	return render(request,'combo/list.html',{'posts': posts })

"""def detail(request):
    question = Post.objects.order_by('-published_date')[:5]
    return render(request, 'combo/detail.html', {'question': question})"""

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'combo/detail.html', {'post': post })


def new(request):
	if request.method == "POST":
		form = BasicForm(request.POST,request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.pub_date = timezone.now()
			post.save()
		posts = Post.objects.filter(published_date=timezone.now()).order_by('published_date')
		return render(request,'combo/list.html' ,{'posts': posts })

            #return redirect('combo:detail', pk=post.pk)
	else:
		form = BasicForm()
		return render(request, 'combo/edit.html', {'form': form})


def edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = BasicForm(request.POST, request.FILES,instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.pub_date = timezone.now()
			post.save()
			return redirect('detail', pk=post.pk)
	else:
		form = BasicForm(instance=post)
	return render(request, 'combo/edit.html', {'form': form})

#poll
def poll(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#template = loader.get_template('combo/poll_index.html')
	context = {
        'latest_question_list': latest_question_list,
    }
	return render(request,'combo/poll_index.html',context)


def polldetail(request, pk):
	try:
		question = Question.objects.get(pk=pk)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'combo/poll_detail.html', {'question': question})



def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'combo/poll_results.html', {'question': question})




def vote(request, pk):
	question = get_object_or_404(Question, pk=pk)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'combo/poll_detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
        })
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('combo:results', args=(question.id,)))