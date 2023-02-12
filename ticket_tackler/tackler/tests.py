from django.test import TestCase
from django.contrib.auth.models import User
from .models import Ticket, Ticket_Comments

class TicketModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.ticket = Ticket.objects.create(
            title='Test Ticket',
            content='Test Content',
            is_open = True,
            type='Bug',
            relevance='Low',
            user=self.user
        )

    def test_ticket_created(self):
        self.assertEqual(Ticket.objects.count(), 1)
        ticket = Ticket.objects.get(title='Test Ticket')
        self.assertEqual(ticket.content, 'Test Content')
        self.assertEqual(ticket.type, 'Bug')
        self.assertEqual(ticket.relevance, 'Low')
        self.assertEqual(ticket.status, 'Open')
        self.assertEqual(ticket.is_open, True)
        self.assertEqual(ticket.user, self.user)
        
    def test_ticket_assigned_to_user(self):
        assigned_user = User.objects.create_user(
            username='assigneduser',
            password='assignedpassword'
        )
        self.ticket.assigned_users.add(assigned_user)
        self.assertEqual(self.ticket.assigned_users.count(), 1)
        self.assertEqual(self.ticket.assigned_users.first(), assigned_user)

class TicketCommentModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.ticket = Ticket.objects.create(
            title='Test Ticket',
            content='Test Content',
            type='Bug',
            is_open = True,
            relevance='Low',
            user=self.user
        )
        self.comment = Ticket_Comments.objects.create(
            content='Test Comment',
            user=self.user,
            ticket=self.ticket
        )

    def test_ticket_comment_created(self):
        self.assertEqual(Ticket_Comments.objects.count(), 1)
        comment = Ticket_Comments.objects.get(content='Test Comment')
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.ticket, self.ticket)