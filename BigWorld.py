# region Private native instance variables

__width = 1920
__height = 1080
__player = None

# endregion

# region Private native classes/types

class __NATIVE_Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

# endregion

class Entity(object):
    pass

def __getAccountInstance():
    try:
        from Account import PlayerAccount
    except ImportError:
        class PlayerAccount(Entity):
            pass
    return PlayerAccount()

def __getAvatarInstance():
    try:
        from Avatar import PlayerAvatar
    except ImportError:
        class PlayerAvatar(Entity):
            pass
    return PlayerAvatar()

def addDecal():
    pass

def addDecalGroup():
    pass

def addIdleCallbackForDelay():
    pass

def addMarkEnterToRegion():
    pass

def addMarkExitFromRegion():
    pass

def addModel():
    pass

def addSpaceGeometryMapping():
    pass

def addTextureFeed():
    pass

def addUPLMessage():
    pass

def addWatcher():
    pass

def allEntities():
    pass

def appendCameraCollider():
    pass

def applyGraphicPreset():
    pass

def autoDetectGraphicsSettings():
    pass

def axisDirection():
    pass

def buildBlueprint():
    pass

def cachedEntities():
    pass

def callback():
    pass

def camera():
    pass

def cameraSpaceID():
    pass

def cameraSpeed():
    pass

def canToDowngradePreset():
    pass

def cancelCallback():
    pass

def changeFullScreenAspectRatio():
    pass

def changeVideoMode():
    pass

def checkAndRecalculateIfPositionInExtremeProjection():
    pass

def checkUnattended():
    pass

def clearAllSpaces():
    pass

def clearBlueprint():
    pass

def clearEntitiesAndSpaces():
    pass

def clearSpace():
    pass

def clearTextureReuseList():
    pass

def clearTextureStreamingViewpoints():
    pass

def collectLastMemoryCriticalEvent():
    pass

def collectMemoryUsage():
    pass

def collide():
    pass

def commandLineLogin():
    pass

def commitPendingGraphicsSettings():
    pass

def component():
    pass

def connect():
    pass

def connectedEntity():
    pass

def consumerBuild():
    pass

def controlEntity():
    pass

def controlPointSetHeight():
    pass

def createBrowser():
    pass

def createEntity():
    pass

def createPlayerEntity():
    pass

def createSpace():
    pass

def createWebView():
    pass

def criticalExit():
    pass

def currentGraphicPresetKey():
    pass

def dcursor():
    pass

def debugDropFilter():
    pass

def debugModel():
    pass

def debugNearPlane():
    pass

def delModel():
    pass

def delSpaceGeometryMapping():
    pass

def delTextureFeed():
    pass

def delWatcher():
    pass

def delaySpaceLoad():
    pass

def destroyBrowser():
    pass

def destroyEntity():
    pass

def destroyWebView():
    pass

def detectGraphicsPresetFromSystemSettings():
    pass

def digest():
    pass

def disconnect():
    pass

def enableBattleStatisticCollector():
    pass

def enableBlueprintBuilding():
    pass

def enableDRRAutoscaling():
    pass

def enableEdgeDrawerVisual():
    pass

def enableFreeCameraModeForShadowManager():
    pass

def enableLoadingTimer():
    pass

def enterSpace():
    pass

def entities():
    pass

def entity():
    pass

def exit():
    pass

def fetchURL():
    pass

def finishDelayedLoading():
    pass

def flushPythonLog():
    pass

def generateGfxSettings():
    pass

def getActiveMonitorIndex():
    pass

def getAspectRatio():
    pass

def getAutoDetectGraphicsSettingsScore():
    pass

def getBattleFPS():
    pass

def getBorderlessParameters():
    pass

def getColorBCSSetup():
    pass

def getColorBrightness():
    pass

def getColorContrast():
    pass

def getColorGradingStrength():
    pass

def getColorSaturation():
    pass

def getDRRAutoscalerBaseScale():
    pass

def getDRRScale():
    pass

def getExclusiveFullscreenMonitorIndex():
    pass

def getExtensionsDirList():
    pass

def getFPS():
    pass

def getFileMappingMemory():
    pass

def getFullScreenAspectRatio():
    pass

def getGammaCorrection():
    pass

def getGenericMemory():
    pass

def getGraphicsPreset():
    pass

def getGraphicsPresetPropertyNames():
    pass

def getGraphicsPresets():
    pass

def getGraphicsPresetsIndices():
    pass

def getGraphicsSetting():
    pass

def getGraphicsSettingApplyMethod():
    pass

def getHeapMemory():
    pass

def getImageMemory():
    pass

def getIsImpassableZoneEnabled():
    pass

def getMaterialKinds():
    pass

def getMemoryInfoKB():
    pass

def getScaleformMemory():
    pass

def getStreamingMemory():
    pass

def getSurfMemory():
    pass

def getSystemPerformancePresetIdFromName():
    pass

def getTextureFeed():
    pass

def getUniProfMemory():
    pass

def getWWiseMemory():
    pass

def getWatcher():
    pass

def getWatcherDir():
    pass

def getWin32HeapMemory():
    pass

def getWindowMode():
    pass

def graphicSetting():
    pass

def graphicSettingIsSupported():
    pass

def graphicsSettings():
    pass

def graphicsSettingsNeedRestart():
    pass

def graphicsSettingsStatus():
    pass

def hangarDestroyed():
    pass

def hangarLoaded():
    pass

def hasPendingGraphicsSettings():
    pass

def importantGraphicSettings():
    pass

def isApplyHighQualityPossible():
    pass

def isArrayDictDataInstance():
    pass

def isClientSpace():
    pass

def isCustomGraphicPreset():
    pass

def isDRRAutoscalingEnabled():
    pass

def isDRRAutoscalingPaused():
    pass

def isDynamicDecalEnabled():
    pass

def isEval():
    pass

def isFixedDictDataInstance():
    pass

def isForwardPipeline():
    pass

def isKeyDown():
    pass

def isNextTickPending():
    pass

def isSSAOEnabled():
    pass

def isShadowsEnabled():
    pass

def isTesselationSupported():
    pass

def isTripleBuffered():
    pass

def isVideoVSync():
    pass

def isWindowVisible():
    pass

def keyToString():
    pass

def leaveSpace():
    pass

def listBorderlessResolutionsAllMonitors():
    pass

def listVideoModes():
    pass

def listVideoModesAllMonitors():
    pass

def loadResourceListBG():
    pass

def loadResourceListFG():
    pass

def lobbyStarted():
    pass

def locale():
    pass

def logCritical():
    pass

def logDebug():
    pass

def logError():
    pass

def logExceptionFrame():
    pass

def logExceptionTraceback():
    pass

def logHack():
    pass

def log():
    pass

def logNotice():
    pass

def logTrace():
    pass

def logWarning():
    pass

def loginEntered():
    pass

def makeScreenshotMarkInReplay():
    pass

def makeWorldMatrix():
    pass

def mapVirtualKey():
    pass

def markerHelperScale():
    pass

def memUsed():
    pass

def memoryDebug():
    pass

def models():
    pass

def notify():
    pass

def notifyBattleTime():
    pass

def notifySpaceChange():
    pass

def objectLod():
    pass

def onInterfaceScaleChanged():
    pass

def overloadBorders():
    pass

def overrideGraphicsSetting():
    pass

def pauseDRRAutoscaling():
    pass

def platform():
    pass

def playMovie():
    pass

def player():
    return __player

# Make IDE think that it can be either Account or Avatar type
__player = __getAccountInstance()
__player = __getAvatarInstance()

def playerDead():
    pass

def printMainLoopTasksOrder():
    pass

def probe():
    pass

def projection():
    pass

def protocolVersion():
    pass

def purgeUrlRequestCache():
    pass

def quit():
    pass

def registerShadowCaster():
    pass

def registerTextureStreamingViewpoint():
    pass

def reinitLoggers():
    pass

def reinitVideoSound():
    pass

def releaseSpace():
    pass

def removeAllIdleCallbacks():
    pass

def removeCameraCollider():
    pass

def resetEntityManager():
    pass

def resetGraphicsSettingsStatus():
    pass

def resetPlayerTargetFrom():
    pass

def resetSettingsUsingDefault():
    pass

def resizeWindow():
    pass

def restartGame():
    pass

def saveAllocationStatsToFile():
    pass

def saveAllocationsToCacheGrindFile():
    pass

def saveAllocationsToFile():
    pass

def saveMemoryUsagePerTexture():
    pass

def savePreferences():
    pass

def screenHeight():
    pass

def screenShot():
    pass

def screenSize():
    pass

def screenWidth():
    pass

def server():
    pass

def serverDiscovery():
    pass

def serverTime():
    pass

def setActiveMonitorIndex():
    pass

def setBorderlessFixedSize():
    pass

def setBorderlessFullscreen():
    pass

def setBorderlessParametersDirect():
    pass

def setBorderlessUnconstrained():
    pass

def setBorderlessWorkAreaMaximized():
    pass

def setColorBCSSetup():
    pass

def setColorBrightness():
    pass

def setColorContrast():
    pass

def setColorGradingStrength():
    pass

def setColorSaturation():
    pass

def setCursor():
    pass

def setDRRScale():
    pass

def setDamageStickerCriticalAngle():
    pass

def setEdgeDrawerImpenetratableZoneOverlay():
    pass

def setEdgeDrawerPenetratableZoneOverlay():
    pass

def setEdgeDrawerRenderMode():
    pass

def setFinalFlushURLRequestsTimeout():
    pass

def setGammaCorrection():
    pass

def setGraphicPresetByIndex():
    pass

def setGraphicPresetByName():
    pass

def setGraphicsSetting():
    pass

def setIsImpassableZoneEnabled():
    pass

def setMinLodBiasForTanks():
    pass

def setPlayerTargetTo():
    pass

def setSpeedTreeCollisionBody():
    pass

def setTextureMinMip():
    pass

def setTextureStreamingMode():
    pass

def setTripleBuffering():
    pass

def setVideoVSync():
    pass

def setWatcher():
    pass

def sinkKeyEvents():
    pass

def solvePow():
    pass

def spaceLoadStatus():
    pass

def spaceTimeOfDay():
    pass

def spaces():
    pass

def startBenchmarkTool():
    pass

def statLagDetected():
    pass

def statPing():
    pass

def stime():
    pass

def stopBenchmarkTool():
    pass

def stopLoadResourceListBGTask():
    pass

def stringToKey():
    pass

def target():
    pass

def targeting():
    pass

def time():
    pass

def timeExact():
    pass

def timeOfDay():
    pass

def trackPhysicsQuality():
    pass

def uniprofRegionEnter():
    pass

def uniprofRegionExit():
    pass

def uniprofSceneStart():
    pass

def unregisterShadowCaster():
    pass

def updateCurrentPresetIndex():
    pass

def updateTerrainBorders():
    pass

def videoModeIndex():
    pass

def virtualTextureRenderComplete():
    pass

# region WG-added methods

def wgAddEdgeDetectCompoundModel():
    pass

def wgAddEdgeDetectDynamicModel():
    pass

def wgAddEdgeDetectEntity():
    pass

def wgAddIgnoredCollisionEntity():
    pass

def wgDelEdgeDetectCompoundModel():
    pass

def wgDelEdgeDetectDynamicModel():
    pass

def wgDelEdgeDetectEntity():
    pass

def wgDelIgnoredCollisionEntity():
    pass

def wgGetBenchmarkLocations():
    pass

def wgSetEdgeDetectEdgeColor():
    pass

def wgSetEdgeDetectPatternColors():
    pass

def wgSetEdgeDetectSolidColors():
    pass

def wg_addDecal():
    pass

def wg_addDecalGroup():
    pass

def wg_addMatkindScaleU():
    pass

def wg_addScaleformTexture():
    pass

def wg_addTempScaleformTexture():
    pass

def wg_addWaterRipples():
    pass

def wg_alloc():
    pass

def wg_applyOverlayToModel():
    pass

def wg_binoculars():
    pass

def wg_bringWindowToForeground():
    pass

def wg_calcGunPitchLimits():
    pass

def wg_changeStringCasing():
    pass

def wg_checkAnyParticlesExist():
    pass

def wg_checkDestructibleIsBush():
    pass

def wg_clearAllScaleformTextures():
    pass

def wg_clearCrashedState():
    pass

def wg_clearDecals():
    pass

def wg_clearTextureReuseList():
    pass

def wg_collectScaleformTextures():
    pass

def wg_collideDynamic():
    pass

def wg_collideDynamicStatic():
    pass

def wg_collideDynamics():
    pass

def wg_collideSegment():
    pass

def wg_collideWater():
    pass

def wg_computeProjectileTrajectory():
    pass

def wg_copyToClipboard():
    pass

def wg_cpdata():
    pass

def wg_cpsalt():
    pass

def wg_crash():
    pass

def wg_createSplineTrack():
    pass

def wg_debugLogging():
    pass

def wg_decalTextureIndex():
    pass

def wg_defaultFlagEmblemCoords():
    pass

def wg_defaultFlagEmblemPath():
    pass

def wg_destroyFallAtom():
    pass

def wg_destroyFragile():
    pass

def wg_destroyModule():
    pass

# Disable lobby FPS limiter
def wg_disableSpecialFPSMode():
    pass

def wg_dumpScaleformMemoryReport():
    pass

def wg_enableGUIBackground():
    pass

def wg_enableInputEvents():
    pass

def wg_enableKeyboardEvents():
    pass

def wg_enableMouseEvents():
    pass

def wg_enableTreeHiding():
    pass

def wg_eraseScaleformResFromCache():
    pass

def wg_eraseScaleformTexture():
    pass

def wg_firstDayOfWeek():
    pass

def wg_free():
    pass

def wg_getCappedShotTargetInfos():
    pass

def wg_getChunkDestrFilenames():
    pass

def wg_getChunkMatrix():
    pass

def wg_getChunkModelFashion():
    pass

def wg_getClientStatistics():
    pass

def wg_getCurrentResolution():
    pass

def wg_getDestructibleEffectCategory():
    pass

def wg_getDestructibleEffectName():
    pass

def wg_getDestructibleEffectScale():
    pass

def wg_getDestructibleEffectsTintColor():
    pass

def wg_getDestructibleFallPitchConstr():
    pass

def wg_getDestructibleFilename():
    pass

def wg_getDestructibleHeight():
    pass

def wg_getDestructibleLifetimeEffectChance():
    pass

def wg_getDestructibleMatrix():
    pass

def wg_getFallingParams():
    pass

def wg_getFrameTimestamp():
    pass

def wg_getHangarStatistics():
    pass

def wg_getHardPointMatrix():
    pass

def wg_getLangCode():
    pass

def wg_getMatInfoNearPoint():
    pass

def wg_getMathInfoUnderPoint():
    pass

def wg_getMaxBorderlessResolution():
    pass

def wg_getMaxWindowedResolution():
    pass

def wg_getMonitorNames():
    pass

def wg_getNMHardPointMatrix():
    pass

def wg_getNativeScreenResoulution():
    pass

def wg_getPreferencesFilePath():
    pass

def wg_getProductVersion():
    pass

def wg_getShotAngles():
    pass

def wg_getShotAnglesNew():
    pass

def wg_getSpaceBounds():
    pass

def wg_getSpaceItemsVisibilityMask():
    pass

def wg_getTimePerFrame():
    pass

def wg_havokExplosion():
    pass

def wg_havokSetSniperMode():
    pass

def wg_havokWipe():
    pass

def wg_initCustomSettings():
    pass

def wg_isCapsLockOn():
    pass

def wg_isDestrCanBeActivated():
    pass

def wg_isHavokActive():
    pass

def wg_isNumLockOn():
    pass

def wg_isSSE2Supported():
    pass

def wg_isScrollLockOn():
    pass

def wg_isSniperModeSwingingEnabled():
    pass

def wg_isVehicleDustEnabled():
    """ Determine whether user enabled dust effects for vehicle
    :returns bool
    """
    return True

def wg_openWebBrowser():
    pass

def wg_precacheScaleformResource():
    pass

def wg_preferencesExistedAtStartup():
    pass

def wg_prefetchSpaceZip():
    pass

def wg_printScaleformCacheStatictics():
    pass

def wg_quitAndStartLauncher():
    pass

def wg_registerDamageSticker():
    pass

def wg_reportSessionData():
    pass

def wg_reportSystemData():
    pass

def wg_resolveFileName():
    pass

def wg_restoreDestructibles():
    pass

def wg_saveWatchers():
    pass

def wg_setAdapterOrdinalNotifyCallback():
    pass

def wg_setAimingParam():
    pass

def wg_setChunkModelFashion():
    pass

def wg_setDestructibleActive():
    pass

def wg_setDestructibleMatrix():
    pass

def wg_setFlagColor():
    pass

def wg_setFlagEmblem():
    pass

def wg_setGUIBackground():
    pass

def wg_setHourOfDay():
    pass

def wg_setMaxFrameRate():
    pass

def wg_setObservableMProv():
    pass

def wg_setPyModelTexture():
    pass

def wg_setRedefineKeysMode():
    pass

def wg_setReducedFpsMode():
    pass

def wg_setScreenshotNotifyCallback():
    pass

def wg_setSpaceItemsVisibilityMask():
    pass

# Enable lobby FPS limiter
def wg_setSpecialFPSMode():
    pass

def wg_setTreeHidingRadius():
    pass

def wg_setWaterFreqX():
    pass

def wg_setWaterFreqZ():
    pass

def wg_setWaterTexScale():
    pass

def wg_setupGroundMaterialsMap():
    pass

def wg_setupMaterialHardness():
    pass

def wg_setupPhysicsParam():
    pass

def wg_simulateProjectileTrajectory():
    pass

def wg_solveDestructibleFallPitch():
    pass

def wg_subscribeToReadPreferences():
    pass

def wg_subscribeToSavePreferences():
    pass

def wg_traceTextureIndex():
    pass

def wg_trajectory_drawer():
    pass

def wg_translateToScaleformKeyCode():
    pass

def wg_ucpdata():
    pass

def wg_unsubAllSavePreferences():
    pass

def wg_updateColorGrading():
    pass

def wg_writeToStdOut():
    pass

# endregion

# TODO: Validate
def windowSize():
    return __NATIVE_Point(__width, __height)

def worldDrawEnabled(newDrawEnabled):
    pass
