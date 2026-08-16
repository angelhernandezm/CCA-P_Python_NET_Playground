namespace Exercises.FactoryPattern;

/// <summary>
/// Common interface implemented by all notification types produced by the factory.
/// </summary>
public interface INotification
{
    string Send(string message);
}

/// <summary>
/// Sends a notification via email.
/// </summary>
public class EmailNotification : INotification
{
    public string Send(string message) => $"Email sent: {message}";
}

/// <summary>
/// Sends a notification via SMS.
/// </summary>
public class SmsNotification : INotification
{
    public string Send(string message) => $"SMS sent: {message}";
}

/// <summary>
/// Sends a notification via push notification.
/// </summary>
public class PushNotification : INotification
{
    public string Send(string message) => $"Push notification sent: {message}";
}

/// <summary>
/// The channels supported by <see cref="NotificationFactory"/>.
/// </summary>
public enum NotificationChannel
{
    Email,
    Sms,
    Push,
}

/// <summary>
/// Factory design pattern exercise.
///
/// Centralizes creation logic for <see cref="INotification"/> implementations so
/// callers depend only on the abstraction, keeping the system open for extension
/// (new channels) and closed for modification (existing call sites don't change).
/// </summary>
public static class NotificationFactory
{
    public static INotification Create(NotificationChannel channel) => channel switch
    {
        NotificationChannel.Email => new EmailNotification(),
        NotificationChannel.Sms => new SmsNotification(),
        NotificationChannel.Push => new PushNotification(),
        _ => throw new ArgumentOutOfRangeException(nameof(channel), channel, "Unsupported notification channel"),
    };
}
