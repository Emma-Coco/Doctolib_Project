import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import correlate, find_peaks

# Charger le fichier CSV
data = pd.read_csv('ecg_data.csv')

# Convertir la colonne 'Timestamp' en objets datetime
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

# Extraire les colonnes timestamp et ECG_value
timestamp = data['Timestamp'].values
ecg_signal = data['ECG_Value'].values
threshold = 0.75

# Supprimer la moyenne du signal ECG pour améliorer la détection de périodicité
ecg_signal_centered = ecg_signal - np.mean(ecg_signal)

# Calcul du pas de temps moyen en secondes
dt = np.mean(np.diff(timestamp).astype('timedelta64[s]').astype(float))
print(f"Pas de temps moyen : {dt:.4f} s")

# Calcul de l'autocorrélation du signal ECG centré
autocorr = correlate(ecg_signal_centered, ecg_signal_centered, mode='full')
lags = np.arange(-len(ecg_signal_centered) + 1, len(ecg_signal_centered)) * dt

# Limiter l'affichage des lags pour éviter les effets de bord
max_lag_seconds = 10
lag_mask = (lags >= 0) & (lags <= max_lag_seconds)
lags_limited = lags[lag_mask]
autocorr_limited = autocorr[lag_mask]

# Trouver les pics dans l'autocorrélation
peaks, _ = find_peaks(autocorr_limited, height=threshold)

# Vérifier si on a trouvé au moins deux pics significatifs
if len(peaks) < 2:
    raise ValueError("Moins de deux pics significatifs trouvés dans l'autocorrélation.")

# Prendre le deuxième pic
second_peak_index = peaks[1]
mean_period = lags_limited[second_peak_index]

# Calculer la fréquence cardiaque correspondante
heart_rate = 1 / mean_period * 60  # Fréquence en battements par minute (BPM)

print(f"Période basée sur le deuxième pic significatif : {mean_period:.2f} s")
print(f"Fréquence cardiaque estimée : {heart_rate:.2f} BPM")

# Découper le signal ECG en segments basés sur la fréquence cardiaque
# Nombre de segments à afficher
num_segments = 5

# Calculer le décalage pour le début du premier segment
segment_start_index = max(0, second_peak_index - 40)  # 30 pas de temps avant le pic

# Longueur du segment (en points)
segment_length = int(mean_period / dt)
print(segment_length)

# Tracer l'autocorrélation et le signal ECG
plt.figure(figsize=(14, 12))

# Tracer l'autocorrélation
plt.subplot(4, 1, 1)
plt.plot(lags_limited, autocorr_limited, label='Autocorrélation')
plt.axhline(y=threshold, color='r', linestyle='--', label='Seuil = 0.75')
plt.axvline(x=mean_period, color='g', linestyle='--', label='Pic détecté à {:.2f}s'.format(mean_period))
plt.plot(lags_limited[second_peak_index], autocorr_limited[second_peak_index], 'ro', markersize=8, label='Deuxième pic retenu')
plt.text(lags_limited[second_peak_index], autocorr_limited[second_peak_index],
         f'Index: {second_peak_index}\nValue: {autocorr_limited[second_peak_index]:.2f}',
         horizontalalignment='left', verticalalignment='bottom', fontsize=10, color='red')
plt.title('Autocorrélation du Signal ECG')
plt.xlabel('Déphasage (s)')
plt.ylabel('Autocorrélation')
plt.legend()

# Tracer le signal ECG complet
plt.subplot(4, 1, 2)
plt.plot(timestamp, ecg_signal)
plt.title('Signal ECG Complet')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')

# Tracer les segments découpés
plt.subplot(4, 1, 3)
for i in range(num_segments):
    start_index = segment_start_index + i * segment_length
    end_index = start_index + segment_length
    if end_index < len(ecg_signal):  # Vérifier que l'index ne dépasse pas la longueur du signal
        # Convertir les timestamps en secondes depuis le début
        start_time = pd.Timedelta(timestamp[start_index] - timestamp[0]).total_seconds()
        end_time = pd.Timedelta(timestamp[end_index - 1] - timestamp[0]).total_seconds()

        plt.plot(timestamp[start_index:end_index], ecg_signal[start_index:end_index],
                 label=f'Segment {i + 1} (de {start_time:.2f}s à {end_time:.2f}s)')
plt.title('Segments ECG Découpés')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.legend()

# Tracer un seul battement de cœur
plt.subplot(4, 1, 4)
start_index = segment_start_index
end_index = start_index + segment_length
if end_index < len(ecg_signal):  # Vérifier que l'index ne dépasse pas la longueur du signal
    # Convertir les timestamps en secondes depuis le début
    start_time = pd.Timedelta(timestamp[start_index] - timestamp[0]).total_seconds()
    end_time = pd.Timedelta(timestamp[end_index - 1] - timestamp[0]).total_seconds()

    plt.plot(timestamp[start_index:end_index], ecg_signal[start_index:end_index],
             label=f'Un battement de cœur (de {start_time:.2f}s à {end_time:.2f}s)')
plt.title('Un Battement de Cœur')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()

# Supposons que mean_period soit déjà calculé
# dt est le pas de temps moyen
dt = np.mean(np.diff(timestamp).astype('timedelta64[s]').astype(float))

# Calculer la longueur de la période en nombre d'échantillons
length_of_period_samples = int(mean_period / dt)

# Imprimer la longueur de la période en échantillons
print(f"La longueur de la période ECG est : {length_of_period_samples} échantillons")
