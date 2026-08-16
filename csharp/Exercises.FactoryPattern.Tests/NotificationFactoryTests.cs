using Exercises.FactoryPattern;

namespace Exercises.FactoryPattern.Tests;

public class NotificationFactoryTests
{
    [Fact]
    public void Create_Email_ReturnsEmailNotification()
    {
        var notification = NotificationFactory.Create(NotificationChannel.Email);

        Assert.IsType<EmailNotification>(notification);
    }

    [Fact]
    public void Create_Sms_ReturnsSmsNotification()
    {
        var notification = NotificationFactory.Create(NotificationChannel.Sms);

        Assert.IsType<SmsNotification>(notification);
    }

    [Fact]
    public void Create_Push_ReturnsPushNotification()
    {
        var notification = NotificationFactory.Create(NotificationChannel.Push);

        Assert.IsType<PushNotification>(notification);
    }

    [Theory]
    [InlineData(NotificationChannel.Email, "Email sent: Hello")]
    [InlineData(NotificationChannel.Sms, "SMS sent: Hello")]
    [InlineData(NotificationChannel.Push, "Push notification sent: Hello")]
    public void Send_ReturnsExpectedMessage(NotificationChannel channel, string expected)
    {
        var notification = NotificationFactory.Create(channel);

        var result = notification.Send("Hello");

        Assert.Equal(expected, result);
    }

    [Fact]
    public void Create_UnsupportedChannel_ThrowsArgumentOutOfRangeException()
    {
        var invalidChannel = (NotificationChannel)999;

        Assert.Throws<ArgumentOutOfRangeException>(() => NotificationFactory.Create(invalidChannel));
    }
}
